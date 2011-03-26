<%
    import public.jsfile as jsfile
    import public.cssfile as cssfile
%>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
    <head>
        <meta content="text/html; charset=utf-8" http-equiv="Content-Type">
        <meta name="description" content="JGuoer Lab是几个Geek组织在一起自发的开发和共享好玩的软件和点子，是一个目标为开发高质量、高性能、低成本的软件团队">
        <meta http-equiv="expires" content="0" />
        <meta name="resource-type" content="document" />
        <meta name="distribution" content="global" />
        <meta name="author" content="JGuo" />
        <meta name="generator" content="jguoer.com" />
        <meta name="copyright" content="Copyright (c) 2010 JGuo. All Rights Reserved." />
        <meta content="no-cache" http-equiv="Pragma">
        <meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7" />
        <meta name="robots" content="index, follow" />
        <meta name="revisit-after" content="1 days" />
        <meta name="rating" content="general" />
        ${self.keywords()}
        ${self.content()}
        <link type="text/css" rel="stylesheet" href="${cssfile.main}" />
        <link type="image/x-icon" href="http://www.jguoer.com/blog/wp-content/themes/jguoer/images/favicon.ico" rel="Shortcut Icon">
        <title>${self.title()}</title>
        <script type="text/javascript" src="${jsfile.jquery}"></script>
        <script type="text/javascript" src="${jsfile.main}"></script>
        <script type="text/javascript">
            ${self.js()}
        </script>
        <style>
            ${self.css()}
        </style>
    </head>

<body>
    <div class="nav clearfix">
        ${self.nav()}
    </div>
    <div class="main clearfix">
        ${self.main()}
    </div>
    <div class="footer">
        ${self.footer()}
    </div>
</body>
</html>

<%def name="title()">JGuoer Lab - 只要心还跳</%def>
<%def name="js()"></%def>
<%def name="css()"></%def>

<%def name="nav()">
    <ul>
        <li><a href="/">主页</a></li>
        <li><a href="/news">新闻</a></li>
        <li><a href="/design">设计</a></li>
        <li><a href="/product">产品</a></li>
        <li><a href="/blog">博客</a></li>
        <li><a href="/about">关于</a></li>
    </ul>
</%def>

<%def name="main()">
</%def>

<%def name="keywords()">
        <meta name="keywords" content="JGuoer,软件工作室,高质量,Python,工作室,Geek" />
</%def>

<%def name="content()">
        <meta name="description" content="JGuoer是一个高质量的软件工作室。" />
</%def>

<%def name="footer()">
Copyright JGuoer 2009-2010 实验室产品 V 0.1.1
</%def>
