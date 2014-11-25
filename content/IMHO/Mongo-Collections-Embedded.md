Title: Collections and Embedded Documents in MongoDB
Date: 2013-10-27 
Tags: NoSQL,Mongo,Zh
Slug: mongo-collections-embdded-think


# MongoDB 中的集合或嵌入式文档

![mongo](https://d262ilb51hltx0.cloudfront.net/max/700/1*cwCnTFQEbcUSy1KvoiIqXg.png)

[via] http://fosterelli.co/collections-and-embedded-documents-in-mongodb.html

When someone is approaching MongoDB from the SQL world, a very common confusion regarding database structure is when to use embedded documents, and when to create an entirely new collection. This distinction is very important because, although MongoDB is schemaless in nature, whether or not an element of your database is structured as embedded documents or a separate collection will change your code a fair amount. Making this change later on can represent a fair amount of work, so it helps to get this right the first time.

There is no "right answer" to this question, as it depends entirely on the situation at hand. The natural tendency of people coming from the SQL world is to stick everything in separate collections, but often this is very unnecessary and will cause serious performance impacts. However, mistakenly placing something within another document may lead to pain further down the road.

A set of rules I have found useful is to ask yourself the following questions:

- Does the embedded document relate to one or more other collections?
- Will you most often need the embedded document without the parent document?
- Will you most often need the parent document without the embedded document?

If the answer to two or more of these is yes, you likely will want a separate collection. If the answer to only one of these is yes, a separate collection should still be considered, but likely not needed.

## Examples

### Comments on a blog

You would like to create a system where people may submit comments on blog posts. The problem is that you are unsure if you should store the comment on the post document, or create a separate collection named comments.

#### Does the embedded document relate to one or more other collections?

No. A comment is typically related to only the post that it is commented on. There may be some situations where this is not true, such as if you provided comment author accounts for editing. However, even this is not a very convincing reason by itself to separate the comment into a separate collection.

#### Will you most often need the embedded document without the parent document?

Again, the answer is no. You likely will not often need to load a comment without also needing the context of the post.

#### Will you most often need the parent document without the embedded document?

In the majority of cases, the answer here is no. Most of the time you use this object, someone will be viewing a blog entry. You will want to both display the post and the comments at once, so it makes sense to fetch those together.

Overall, comments for a blog is a very good candidate for embedded documents.

### Students in a class

You have a school management system, and you would like to enable students to enrol in a particular class. You are unsure if you should store the student objects on the class, or create a separate collection named students.

#### Does the embedded document relate to one or more other collections?

Typically, we can assume yes. A student will likely relate to other things, such as an assignment or school object. Also, a very important note is that each embedded document will likely relate to multiple documents in the classes collection, which is a very strong hint you need a separate collection.

###3 Will you most often need the embedded document without the parent document?

The answer here will often be yes. If you want any sort of student information panel or want to have students enrolled in different classes, then you will often want the student document without needing the context of each class.

#### Will you most often need the parent document without the embedded document?

Probably no for this one. It depends on what operation we are doing most often with the class, but I imagine that when we fetch a class we would likely need at least one student as well.

Overall, students in a class are probably better suited for a separate collection. It's important to keep in mind the scope of the problem you are solving with the data, and the operations that will be done most commonly. That said, a student is a very relational piece of data and better fits a separate collection.

>>> 尝试翻译为中文:


如果刚刚从SQL 世界进入 MongoDB, 最常见的困惑就是 "嵌入式文档" 以及何时创建新的"集合"?
这类困惑的根源就是还没有建立起来 MongoDB 的自由结构世界观 ;-)
SQL 世界的来客,总是试图先建立起一个完美的关系体系可以兼容以后的所有业务变化, 而 Mongo们,则是更加愿意先将已知的数据舒服的收集起来,随着业务的理解,不断的调整结构,同时代码永远可用!

那么,这里给出俺知道的判定问题:

- 嵌入的文档,同其它集合有一个或以上的关联嘛?
- 你将总会请求嵌入的文档,而 不需要 父文档嘛?
- 你将总会请求父文档,而 不需要 嵌入的文档嘛?

如果以上问题,有两个或以上回答为 yes, 那么最好使用独立的集合.
如果回答只有一个为 yes, 那么独立集合也应该考虑,但一般不必要了.

## 示例

### blog 的评注
你可能创建过类似blog 的系统,允许用户创建评注.问题在于你无法确定这堆评注,是存储在文章对象中呢,还是另外创建集合来保存?
动用以上问题来考查一下... 

#### 嵌入的文档,同其它集合有一个或以上的关联嘛?

首先呢,评注肯定是先同当前文章有关联的. 同时也有很多其它方案, 比如想支持作者可以修订评注. 但是,这还不足以今评注分离成独立集合.

你将总会请求嵌入的文档,而 不需要 父文档嘛?

再来,如果这问题的回答是 否. 意味着你并不想加载文章时,一定就显示评注.

#### 你将总会请求父文档,而 不需要 嵌入的文档嘛?

多数情况,这个问题的回答是 否. 一般只是想显示文章, 只是有时,期望同时显示, 那就必须让这一动作简单.

综上, 评注作为 嵌入文档 是合理的.

## 班级中的学生
你有个学校管理系统, 想让学生作为特殊的一个类, 但是,不肯定是作为班级的嵌入文档呢, 还是独立集合.

#### 嵌入的文档,同其它集合有一个或以上的关联嘛?

典型的,我们回答 是 . 每个学生总是会关联各种事物, 比如学校.同时,重要的每个嵌入文档同多个班级有关系时,这是分离为单独集合的重要暗示.

#### 你将总会请求嵌入的文档,而 不需要 父文档嘛?

这问题经常回答为 是. 如果你想对学生进行多种排序,或是不同班级有不同学生参加,所以你总是想使用 学生节点而不是班级的信息.

#### 你将总会请求父文档,而 不需要 嵌入的文档嘛?

这问题可能就是 否了. 这取决于我们经常怎么使用班级的数据, 目测其实我们最常查询班级的数据就是最后那名学生是谁.

综上,班级学生最好分离为独立的集合. 重要的是问题域要关注你的数据,并且令数据分布吻合常见事务要求. 即, 学生关联那多数据,最好独立!

that all!

其实, 使用文档型NoSQL, 特别是 MongoDB, 放弃RMDB 那堆范式的概念,使用我们的直觉,从当前已知的常见操作出现来设计文档结构就对了!

## Changelog

- 140107 move into Pelican as zoomquiet.io
- 131027 pub. [Collections and Embedded Documents in MongoDB — I. M. H. O. — Medium](https://medium.com/i-m-h-o/c161d7036f89)
