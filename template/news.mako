<%inherit file="/base.mako"/>
<%def name="main()">
%if not articles or not len(articles):
    稍后整理上传。
%else:
    %for a in articles:
    <div class="item">
        <%
            time = a.time
            title = a.title
        %>
        %if a.url:
        <a href="${a.url}">${title}</a> - ${time}
        %else:
        <a href="/article/${a.id}">${title}</a> - ${time}
        %endif
    </div>
    %endfor
%endif
</%def>

