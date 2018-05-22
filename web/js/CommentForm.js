const commentForm = {rows: [
    {
        view: 'form',
        id: 'win1',
        elements: [{
            view: 'text',
            label: 'Comment',
            name: 'comment',

        },
        {
            view: 'button',
            value: 'Submit',
            click: function() {
                alert('comment submitted')
            }
        }],
        elementsConfig: {
            labelPosition: 'top',
        }
    },
]
}
