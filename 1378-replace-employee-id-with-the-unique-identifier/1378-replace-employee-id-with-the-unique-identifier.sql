select em.unique_id as unique_id, e.name as name
from Employees e
left join  EmployeeUNI em on em.id = e.id; 