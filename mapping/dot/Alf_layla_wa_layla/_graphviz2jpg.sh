#! /bin/sh
#=========================================================== action bath

# 检查参数个数
if [ $# -ne 1 ]; then
  echo "Usage: $0 path/2/dotfile (not .dot)"
  echo "e.g: ./_graphviz2jpg.sh Alf_layla_wa_layla0010"
  exit 1
fi


dotname="$1" #"vlog-chaos42-hedyCSS.dark.jpeg"
# 参数检查ok,执行程序
echo "dot -Tjpeg $dotname.dot -o $dotname.jpg"
#exit  0

dot -Tjpeg $dotname.dot -o $dotname.jpg
#=========================================================== action DONE
#exit  0


