<%inherit file="/base.mako"/>
<%def name="main()">
%if not users:
暂时还没有人写博客..<br/>
返回<a href="http://www.jguoer.com/blog">郭靖的博客</a>
%else:
    <div class="selecttab clearfix">
    <ul>
    <li class="current" name="all">所有</li>
    %for i,user in enumerate(users):
        <li name="${user.name}">${user.nickname}</li>
    %endfor
    </ul>
    </div>
    <div class="blog">
        %for user in users:
            <div id="${user.name}" class="all">
            <div class="author">${user.nickname}</div>
            %if user.rss:
                %for r in user.rss:
                    <div class="item"><a href="${r.link}" target="_blank">${r.title}</a></div>
                %endfor
            %else:
            <div class="item">暂时无法取到Ta的博客:( >>去<a href="${user.blog_url}" target="_blank">Ta的博客</a></div>
            %endif
            </div>
        %endfor
    </div>
%endif
<script>
$(document).ready(function(){
    $(".selecttab ul li").click(function(){
        name = $(this).attr("name");
        $(".selecttab ul li").removeAttr("class");
        $(this).attr("class", "current");
        if (name=="all"){
            $(".all").show();
        } else {
            $(".all").hide();
            $("#"+name).show();
        }
    });
})
</script>
</%def>
