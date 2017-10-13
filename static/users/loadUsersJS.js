String.prototype.format = function()
{
    var args = arguments;
    return this.replace(/\{(\d+)\}/g,
        function(m,i){
            return args[i];
        });
}

$.ready.then(function(){
    $('#get-btn').click(function () {
        $.get('/api/users/?format=json', function (obj) {
            $('#plain-json').html(JSON.stringify(obj));
            var html = '';
            for(var i=0; i<obj.length; ++i)
            {
                var user = obj[i];
                html += '<tr><th>{0}</th><th>{1}</th><th>{2}</th><th>{3}</th></tr>'
                    .format(user['url'], user['username'], user['email'], user['groups']);
            }
            $('#table-body').html(html);
        }, 'json');
    });
});