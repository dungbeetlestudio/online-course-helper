var main = async () => {
    var app = require('./express')
    require('./robots').init(app)

    app.all(/test/, function (req, res) {
        res.setHeader('Access-Control-Allow-Credentials', true)
        res.setHeader('Access-Control-Allow-Origin', '*')
        console.log(req.query)
        console.log(req.body)
        res.send('hello world')
    })

    app.listen(10000, function () {
        console.log('HTTP Server is running on: http://www.dungbeetles.xyz')
    })
}

main()