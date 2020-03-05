Title: Elixir 中列出 Map 中值键对的折腾...
Date: 2020-01-08
Tags: Elixir,FAQ,sayeahooo
Slug: 200108-ex-map-enum

[TOC]


因为各种原因吧...

- 很早在 ECUG 就接触了 Erlang
    + 但是, 怪异的语法,以及狭小的应用领域,一直没真正使用起来
    + 现在, 发现 Elixir 很好的解决了 OTP 生态的通用应用问题
- 所以, 开始折腾...
- 结果, 撞见各种值得嗯哼的事儿...

## env.

༄  screenfetch

                     -/+:.          zoomq@ZQ160626rMBP
                    :++++.          OS: 64bit Mac OS X 10.12.6 16G2136
                   /+++/.           Kernel: x86_64 Darwin 16.7.0
           .:-::- .+/:-``.::-       Uptime: 30d 12h 38m
        .:/++++++/::::/++++++/:`    Packages: 241
      .:///////////////////////:`   Shell: bash
      ////////////////////////`     Resolution: 2560x1440
     -+++++++++++++++++++++++`      DE: Aqua
     /++++++++++++++++++++++/       WM: Quartz Compositor
     /sssssssssssssssssssssss.      WM Theme: Blue
     :ssssssssssssssssssssssss-     CPU: Intel Core i7-5557U @ 3.10GHz
      osssssssssssssssssssssssso/`  GPU: Intel Iris Graphics 6100
      `syyyyyyyyyyyyyyyyyyyyyyyy+`  RAM: 9318MiB / 16384MiB
       `ossssssssssssssssssssss/
         :ooooooooooooooooooo+.
          `:+oo+/:-..-:/+o+/-



- Erlang/OTP 21 [erts-10.2] [source] [64-bit] [smp:4:4] [ds:4:4:10] [async-threads:1] [hipe]
- Elixir 1.9.1 (compiled with Erlang/OTP 20)


## problem
> 使用 Plug 快速开发 Slack 插件...

首先得完成基于 Plug 的 API 服务,
这其中最关键的是从 GET/POST 协议请求中获得 Slack 转发过来的用户指令;

官方文档中 demo 形似:

    defmodule Example.Plug.VerifyRequest do
      defmodule IncompleteRequestError do
        @moduledoc """
        Error raised when a required field is missing.
        """

        defexception message: ""
      end

      def init(options), do: options

      def call(%Plug.Conn{request_path: path} = conn, opts) do
        if path in opts[:paths], do: verify_request!(conn.params, opts[:fields])
        conn
      end

      defp verify_request!(params, fields) do
        verified =
          params
          |> Map.keys()
          |> contains_fields?(fields)

        unless verified, do: raise(IncompleteRequestError)
      end

      defp contains_fields?(keys, fields), do: Enum.all?(fields, &(&1 in keys))
    end


对应检验请求可以是:

    $ curl localhost:8080/upload?content=foo&mimetype=bar

问题是:

    ...
    |> contains_fields?(fields)


- 提供的函式只是对所有 URI 参数键进行检验, 如果缺少了则报错,
- 可是, 正确请求时, 如何获得所有参数值?

先使用输出语句来探查 params 是什么数据类型:

    IO.inspect(params)

请求触发后终端输出:

    %{"cnt" => "foo", "mmt" => "bar"}

是标准 Map 对象.

## try
> Enum.all?() 是个重要的入口

追查文档, 知道 Enum 有丰富的序列型数据处置支持:

> Enum.each 可以针对每个键进行附加处置

所以:

    defp echo_vars(keys, fields) do 
        Enum.each(fields, fn(s) -> IO.puts(s) end)
        LOG.info("chk. as #{keys} ;-)")
    end

但是, 各种出错, 因为这时, 传入的 keys 是只有请求 Map 中的键;

那么:

    Enum.each(params,fn(k) -> IO.puts(Map.get(params,k)) end)

- 跳出 verified = params ... 的处理流水线;
- 直接追加列印处理?
- 也不行...
    + 光是看形式就有问题
    + 先对 Map 进行 Enum.each 
    + 然后对每一个键, 再进行 Map.get
    + 这简直是对相同的数据进行反复操作

## Hummm?!
> 万万没想到...

无意中在 [如何在Elixir中将映射键从字符串转换为原子 | 码农俱乐部 - Golang中国 - Go语言中文社区](https://mlog.club/article/1923002)

看到:

    iex(1)> string_key_map = %{"foo" => "bar", "hello" => "world"}
%{"foo" => "bar", "hello" => "world"}

    iex(2)> for {key, val} <- string_key_map, into: %{}, do: {String.to_atom(key), val}
    %{foo: "bar", hello: "world"}

虽说这是 Comprehensions 概念的通常使用,
但是, 发现, for 这个操作, 和 Python 中的完全一致哪,
于是:

      defp echo_vars(params) do
        for {key, val} <- params do
          #IO.inspect(key)
          #IO.inspect(val)
          LOG.info("each -> #{key}=>#{val} ;-)")
        end
      end

简直和 Python 中解包行为完全一致...

可是: [Learn elixir in Y Minutes](https://learnxinyminutes.com/docs/zh-cn/elixir-cn/)
一句也没提及, for 这么 NB 的操作符哪...

## refer.

- [Plug.Router — Plug v1.8.3](https://hexdocs.pm/plug/Plug.Router.html)
    + [Plug · Elixir School](http://elixirschool.com/zh-hans/lessons/specifics/plug/)
- [如何在Elixir中将映射键从字符串转换为原子](https://mlog.club/article/1923002)
    + [Elixir入门教程－速构 | Time is all](https://szpzs.oschina.io/2017/02/11/elixir-getting-started-comprehensions/)



## Changelog

- 200109 .5h 配置模板,重新发布
- 200108 .5h 输出
- 200107 2.5h 折腾
