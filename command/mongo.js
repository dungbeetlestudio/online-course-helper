var mc = require('mongodb').MongoClient

console.log('init mongodb.')

module.exports.init = async () => {
    var mongo = await mc.connect('mongodb://www.dungbeetles.xyz:27017')
    var db = mongo.db('dungbeetles')
    var peoples = db.collection('online-course-helper')
    return peoples
}