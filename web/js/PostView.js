var form = {
    view: 'form',
    id: 'win1',
    borderless: true,
    elements: [{
        view: 'text',
        label: 'Comment',
        name: 'comment'
    },
    {
        view: 'button',
        value: 'Submit',
        click: function() {}
    }
    ],
    elementsConfig: {
        labelPosition: 'top',
    }
};

var content = `
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
no sea takimata sanctus est Lorem ipsum dolor sit amet.
`
const postView = {
    view: 'scrollview',
    scroll: 'y',
    body: {
        rows: [{
            view: 'template',
            width: '100%',
            height: 70,
            css: 'largeText',
            template: 'TITLE',
        },
        {
            view: 'template',
            width: '100%',
            height: 25,
            template: 'AUTHOR_ID / Created on: CREATION_DATE / Last edited: EDIT_DATE',
        },
        {
            view: 'template',
            height: 500,
            template: 'PHOTO_PLACEHOLDER'
        },
        {
            view: 'template',
            width: '100%',
            height: 200,
            template: content + content + content
        },
        {
            view: 'template',
            height: 30,
            template: '(#) Comments'
        },
        {
            view: 'button',
            width: 100,
            value: 'Comment',
            click: function() {
                $$('win1').getBody().clear();
                $$('win1').show(this.$view);
                $$('win1').getBody().focus();
            }
        },
        {
            body: {
                rows: [
                    commentForm
                ]
            }
        },

        {
            body: {
                rows: [
                    commentView, commentView, commentView 
                ]
            }
        },
        ]
    }
};

