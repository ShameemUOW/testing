DELIMITER //

CREATE TRIGGER before_employee_clock_in
BEFORE INSERT ON Attendance
FOR EACH ROW
BEGIN
    DECLARE existing_attendance INT;
    
    -- Check if there is an existing attendance entry for the employee with no clock-out time
    SELECT COUNT(*)
    INTO existing_attendance
    FROM Attendance
    WHERE EmployeeID = NEW.EmployeeID AND ClockOut IS NULL;
    
    -- If an existing entry with no clock-out time is found, prevent the new clock-in entry
    IF existing_attendance > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Employee has an active attendance entry. Clock out first.';
    END IF;
END //

DELIMITER ;

DELIMITER //

CREATE TRIGGER before_employee_clock_out
BEFORE INSERT ON Attendance
FOR EACH ROW
BEGIN
    DECLARE existing_attendance INT;
    
    -- Check if there is an existing clock-in entry for the employee
    SELECT COUNT(*)
    INTO existing_attendance
    FROM Attendance
    WHERE EmployeeID = NEW.EmployeeID AND ClockOut IS NULL;
    
    -- If no clock-in entry is found, prevent the new clock-out entry
    IF existing_attendance = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Employee must clock in before clocking out.';
    END IF;
END //

DELIMITER ;