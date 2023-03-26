UPDATE objects
    SET
        ParentProjectId = '$ParentProjectId',
        Name = '$Name',
        Status = '$Status',
        PercentComplete = '$PercentComplete',
        SystemStartDate = '$SystemStartDate',
        SystemEndDate = '$SystemEndDate',
        PlannedStartDate = '$PlannedStartDate',
        PlannedEndDate = '$PlannedEndDate',
        ActualStartDate = '$ActualStartDate',
        ActualEndDate = '$ActualEndDate',
        OwnerId = '$OwnerId',
        ResponsibleId = '$ResponsibleId'

    WHERE UID='$UID' LIMIT 1