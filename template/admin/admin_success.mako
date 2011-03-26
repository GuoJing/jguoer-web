<%inherit file="/base.mako"/>

<%def name="main()">
<%
    text = success_text or '操作执行成功'
    link = return_url or '/'
%>
${text}<br/>
<a href="${link}">返回</a>
</%def>
