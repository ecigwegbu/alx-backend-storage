db.students.aggregate([
    {
        $unwind: '$topics'
    },
    {
        $group: {
            name: '$name',
            averageScore: {$avg: '$topics.score' }
        }
    },
    {
        $sort: {
            averageScore: -1
        }
    }
]}
