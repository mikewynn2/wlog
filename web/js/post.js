webix.ready(function() {
    webix.ui({
        id: 'posts',
        scroll: true,
        rows:[
            {
                view:'template',
                width: '100%',
                height: 50,
                header: true,
                css: 'wlog_title',
                template: '<div class="wlog_title">Welcome to the Wlog</div>'
            },
            {
                view:'template',
                width: '100%',
                height: 50,
                header: true,
                css: 'largeText',
                template:'This will be the post title' 
            },
            {
                view: 'template',
                width: '100%',
                height: 25,
                header: false,
                template: 'created on (date) By: (authod id)'

            },
            {
                view: 'template',
                width:'100%',
                height: 25,
                template: '#of comments',
            },
            {
                view: 'template',
                width: '25%',
                height: 200,
                css: 'wlog_title',
                template: 'this is going to be a picture',
            },
            {
                view: 'template',
                width: '100%',
                height: 350,
                template: 'This is the content of the post, it will be much longer'
            },
            {
                view: 'template',
                width:'100%',
                height: 10,
                template: '',
                css: 'spacer',

            },
            {
                view:'template',
                width: '100%',
                height: 50,
                header: true,
                css: 'wlog_title',
                template: '<div class="wlog_title">Comments</div>'
            },
            {
                view:'list',
                width: '100%',
                height: 500,
                scroll: true,
                template:'comment 1'
            },
        ]
    })
});
