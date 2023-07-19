db.nginx.aggregate(
    [
        {
            $group:
                {
                    _id: '$ip',
                    count: {$sum: 1}
                }
        },
        {
            $sort: { count: -1 }
        },
        {
            $limit: 10
        }
    ]
)
