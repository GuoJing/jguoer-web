<%inherit file="/base.mako"/>
<%namespace name="utils" file="/widgets/banner.mako" />

<%def name="main()">
${utils.banner(user.name)}
%if not articles or not len(articles):
    你还没有文章
%else:
    %for a in articles:
    <div class="item" id="item${a.id}">
        <%
            time = a.time
            title = a.title
        %>
        %if a.url:
        <a href="${a.url}">${title}</a> <a class="remove" href="/admin/delete/${a.id}">X</a>
        %else:
        <a href="/admin/edit/${a.id}">${title}</a> <a class="remove" href="/admin/delete/${a.id}">X</a>
        %endif
    </div>
    %endfor
%endif
</%def>
