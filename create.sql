-- For PostgreSQL database cs101quiz
-- Author: Alexander Bendeck on 10/8/2019

CREATE TABLE Questions
(qid INTEGER NOT NULL PRIMARY KEY,
 concept VARCHAR(256) NOT NULL,
 function VARCHAR(256),
 text VARCHAR(256) NOT NULL,
 correct_ans VARCHAR(256) NOT NULL,
 wrong_ans_1 VARCHAR(256) NOT NULL,
 wrong_ans_2 VARCHAR(256),
 wrong_ans_3 VARCHAR(256));

CREATE TABLE Students
(netid VARCHAR(6) NOT NULL PRIMARY KEY,
 email VARCHAR(256) NOT NULL UNIQUE,
 name VARCHAR(256) NOT NULL,
 lab_section INTEGER NOT NULL);

CREATE TABLE Responses
(rid INTEGER NOT NULL PRIMARY KEY,
 netid VARCHAR(6) NOT NULL
	REFERENCES Students(netid),
 qid INTEGER NOT NULL
	REFERENCES Questions(qid),
 ans_choice VARCHAR(256) NOT NULL,
 timestamp VARCHAR(256) NOT NULL);

CREATE FUNCTION TF_Answer_Valid() RETURNS TRIGGER AS $$
BEGIN
  IF NOT EXISTS (SELECT * FROM Questions AS Q
                      WHERE NEW.qid = Q.qid
                        AND NEW.ans_choice = Q.correct_ans
                        OR NEW.ans_choice = Q.wrong_ans_1
                        OR NEW.ans_choice = Q.wrong_ans_2
                        OR NEW.ans_choice = Q.wrong_ans_3)
  THEN
    RAISE EXCEPTION 'Answer choice not valid for that question';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER TG_Answer_Vaid
  BEFORE INSERT OR UPDATE ON Responses
  FOR EACH ROW
  EXECUTE PROCEDURE TF_Answer_Valid();
