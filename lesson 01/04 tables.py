x = int(input('в первом классе:',));
y = int(input('во втором классе:',));
z = int(input('в третьем классе:',));
tablse_x = x//2+x%2;
tables_y = y//2+y%2;
tables_z = y//2+z%2;
tables = tablse_x + tables_y + tables_z;
print ('Всего требуется парт:', tables);
