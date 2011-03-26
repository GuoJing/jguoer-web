<%!
    from lib.utils import replace_html
    from public.consts import user_info
%>
<%inherit file="/base.mako"/>
<%namespace name="utils" file="/widgets/banner.mako" />
<%def name="main()">
${utils.banner(sname)}
%if not articles.count():
    好像没有这个文章
%else:
    %for a in articles:
    <form action="/admin/article?ask=${ask}" method="POST">
    <div class="item">
        <%
            time = str(a.time.year) + "-" + str(a.time.month) + "-" + str(a.time.day)
            title = a.title.encode('utf-8')
            content = a.content.encode('utf-8').replace('\n',"<br/>")
            name = a.author
            info = user_info[name].split(',')
            nickname = info[0]
            pic = info[1]
        %>
        <input type="text" class="input" value="${title or ''}" name="title"/><br/>
        <input type="text" class="input" value="${time}" name="time" readonly="true"/>
        <div class="content">
        <textarea name="content" class="textarea">${content.replace('<br/>','') or ''}</textarea>
        <input type="submit" value="提交"/> <span class="error">${error or ''}</span>
        </div>
    </div>
    %endfor
%endif
</%def>

<%def name="css()">
.avatar {
    margin-left:5px;
}
</%def>
