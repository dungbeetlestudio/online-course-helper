var mc = require('mongodb').MongoClient

var main = async () => {
    console.log('init mongodb.')

    var mongo = await mc.connect('mongodb://www.dungbeetles.xyz:27017/', { useNewUrlParser: true })

    var db = mongo.db('online-course-helper')
    var peoples = db.collection('peoples')

    await peoples.insertOne({
        name: 'truman',
        saySomething: ['hahahah'],
        qusations: ['+1'],
        robots: [
            { account: "517013400", pwd: "xfskyl6422", order: [{ f: '', v: '' }], ready: true, hasSigns: {} },
            { account: "614332022", pwd: "xfskyl6422", order: [{ f: '', v: '' }], ready: true, hasSigns: {} }
        ]
    })

    await mongo.close()
}

main()
