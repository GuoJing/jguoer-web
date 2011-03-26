<%inherit file="/base.mako"/>
<%def name="main()">
%if not articles.count():
    稍后整理上传。
%else:
    %for a in articles:
    <div class="item">
        <%
            time = str(a.time.year) + "-" + str(a.time.month) + "-" + str(a.time.day)
            title = a.title.encode('utf-8')
        %>
        %if a.url:
        <a href="${a.url}">${title}</a> - ${time}
        %else:
        <a href="/article?ask=${a.aid}">${title}</a> - ${time}
        %endif
    </div>
    %endfor
%endif
</%def>
