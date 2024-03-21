-- creates stored procedure that computes and stores average score for students
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users AS U, 
        (SELECT U.id, SUM(score * weight) / SUM(weight) AS weightedAvg
        FROM users AS U 
        JOIN corrections as C ON U.id=C.user_id 
        JOIN projects AS P ON C.project_id=P.id 
        GROUP BY U.id)
    AS WA
    SET U.average_score = WA.weightedAvg WHERE U.id=WA.id;
END $$
DELIMITER ;
