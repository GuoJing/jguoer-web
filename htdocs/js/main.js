$(document).ready(function(){
    set_login_form();
    set_article_form();
    set_edit_form();
    set_remove();
    set_comment_form();
});

function set_login_form(){
   $('#loginform').submit(function(e){
        e.preventDefault();
        name = $('#name').val();
        pwd  = $('#pwd').val();
        err  = $('.error');
        if (name == '' || pwd == ''){
            err.html('用户名或密码不能为空..');
            return;
        }
        err.html('');
        $.post('/admin/login', {'name' : name,'pwd' : pwd}, function(ret){
            if(ret.r && ret.authen) {
                window.location.href = '/admin/main';
            } else {
                err.html('认证失败..');
            }
        }, 'json')
    }); 
}

function set_article_form(){
    $('#addart').submit(function(e){
        e.preventDefault();
        title = $('#title').val();
        cate = $('#addart').attr('st');
        url = $('#url').val();
        content = $('#content').val();
        if(title == '') {
            $('.error').html('标题不能为空');
            return;
        }
        $('.error').html('');
        $.post('/admin/add', {'title' : title, 'cate': cate, 'url' : url, 'content' : content}, function(ret){
            if(ret.r && ret.ok) {
                window.location.href = '/admin/success';
            } else {
                $('.error').html('文章发布错误');
            }
        }, 'json')
    });
    $("textarea").click(function(){
        $(".info").html($(this).attr('desc'));
    });
    $("input[name='cate']").click(function(){
        $(".info").html($(this).attr('desc'));
        $('#addart').attr('st', $(this).val());
        $('#editart').attr('st', $(this).val());
    });
    $($("#addart input[name='cate']")[0]).attr('checked', 'true');
}

function set_remove(){
    $('.remove').click(function(){
        url = $(this).attr('href');
        $.post(url,{},function(ret){
            if(ret.r){
                $('#item'+ret.id).fadeOut();
            }
        },'json');
        return false;
    });
}

function set_comment_form() {
    $('.show_reply').click(function(){
        $(this).hide();
        $('.reply_form').show('slow');
    });
}

function set_edit_form() {
    $('#editart').submit(function(e){
        e.preventDefault();
        title = $('#title').val();
        cate = $('#editart').attr('st');
        aid = $('#editart').attr('aid');
        url = $('#url').val();
        content = $('#content').val();
        if(title == '') {
            $('.error').html('标题不能为空');
            return;
        }
        $('.error').html('');
        $.post('/admin/edit/' + aid, {'title' : title, 'cate': cate, 'url' : url, 'content' : content}, function(ret){
            if(ret.r && ret.ok) {
                window.location.href = '/admin/success';
            } else {
                $('.error').html('文章发布错误');
            }
        }, 'json');
    });
    $($("#editart input[name='cate']")[0]).removeAttr('checked');
}
