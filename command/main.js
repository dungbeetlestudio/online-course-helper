var main = async () => {
    var app = require('./express')
    require('./robots').init(app)

    app.all(/test/, function (req, res) {
        res.setHeader('Access-Control-Allow-Credentials', true)
        res.setHeader('Access-Control-Allow-Origin', '*')
        console.log(req.query)
        console.log(req.body)
        res.send([])
    })

    app.listen(80, function () {
        console.log('HTTP Server is running on: http://localhost:%s', 80)
    })
}

main()