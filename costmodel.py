import sqlite3

def create_cost_table():
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    """Table cost creation"""
    create_table = '''
                 CREATE TABLE IF NOT EXISTS CostTable (
                 id INTEGER PRIMARY KEY,
                 FenceCode TEXT,   
                 FenceDescription TEXT,
                 Height REAL,
                 Thickness REAL,
                 APPATURE INTEGER,
                 COST REAL   
                 );
                 '''
    cursor.execute(create_table)
    
    """Insert Data Query"""
    insert_table = '''
                    INSERT INTO CostTable (FenceCode, FenceDescription, height, Thickness, APPATURE, COST)
                    VALUES(?,?,?,?,?,?);
                   '''
    data_insert_table = [
                        ('DM0950L30', 'diamond mesh', 0.9, 2, 50, 0.75 ),
                        ('DM1250L30', 'diamond mesh', 1.2, 2, 50, 0.80 ),
                        ('DM1550L30', 'diamond mesh', 1.5, 2, 50, 0.85 ),
                        ('DM1850L30', 'diamond mesh', 1.8, 2, 50, 0.90 ),
                        ('DM2150L30', 'diamond mesh', 2.1, 2, 50, 0.95 ),
                        ('DM2750L30', 'diamond mesh', 2.7, 2, 50, 1.00 ),
                        ('DM0950H30', 'diamond mesh', 0.9, 2.5, 50, 1.20 ),
                        ('DM1250H30', 'diamond mesh', 1.2, 2.5, 50, 1.25 ),
                        ('DM1550H30', 'diamond mesh', 1.5, 2.5, 50, 1.30 ),
                        ('DM1850H30', 'diamond mesh', 1.8, 2.5, 50, 1.35 ),
                        ('DM2150H30', 'diamond mesh', 2.1, 2.5, 50, 1.40 ),
                        ('DM2450H30', 'diamond mesh', 2.4, 2.5, 50, 1.45 ),
                        ('DM2750H30', 'diamond mesh', 2.7, 2.5, 50, 1.50 ),
                        ('DM0950HX30', 'diamond mesh', 0.9, 3.15, 50, 1.75 ),
                        ('DM1250HX30', 'diamond mesh', 1.2, 3.15, 50, 1.80 ),
                        ('DM1550HX30', 'diamond mesh', 1.5, 3.15, 50, 1.90 ),
                        ('DM1850HX30', 'diamond mesh', 1.8, 3.15, 50, 2.00 ),
                        ('DM2150HX30', 'diamond mesh', 2.1, 3.15, 50, 2.10 ),
                        ('DM2450HX30', 'diamond mesh', 2.4, 3.15, 50, 2.20 ),
                        ('DM2750HX30', 'diamond mesh', 2.7, 3.15, 50, 2.30 ),
                        ('DM0975L30', 'diamond mesh', 0.9, 2, 75, 0.75 ),
                        ('DM1275L30', 'diamond mesh', 1.2, 2, 75, 0.80 ),
                        ('DM1575L30', 'diamond mesh', 1.5, 2, 75, 0.85 ),
                        ('DM1875L30', 'diamond mesh', 1.8, 2, 75, 0.90 ),
                        ('DM2175L30', 'diamond mesh', 2.1, 2, 75, 0.95 ),
                        ('DM2775L30', 'diamond mesh', 2.7, 2, 75, 1.00 ),
                        ('DM0975H30', 'diamond mesh', 0.9, 2.5, 75, 1.20 ),
                        ('DM1275H30', 'diamond mesh', 1.2, 2.5, 75, 1.25 ),
                        ('DM1575H30', 'diamond mesh', 1.5, 2.5, 75, 1.30 ),
                        ('DM1875H30', 'diamond mesh', 1.8, 2.5, 75, 1.35 ),
                        ('DM2175H30', 'diamond mesh', 2.1, 2.5, 75, 1.40 ),
                        ('DM2475H30', 'diamond mesh', 2.4, 2.5, 75, 1.45 ),
                        ('DM2775H30', 'diamond mesh', 2.7, 2.5, 75, 1.50 ),
                        ('DM0975HX30', 'diamond mesh', 0.9, 3.15, 75, 1.75 ),
                        ('DM1275HX30', 'diamond mesh', 1.2, 3.15, 75, 1.80 ),
                        ('DM1575HX30', 'diamond mesh', 1.5, 3.15, 75, 1.90 ),
                        ('DM1875HX30', 'diamond mesh', 1.8, 3.15, 75, 2.00 ),
                        ('DM2175HX30', 'diamond mesh', 2.1, 3.15, 75, 2.10 ),
                        ('DM2475HX30', 'diamond mesh', 2.4, 3.15, 75, 2.20 ),
                        ('DM2775HX30', 'diamond mesh', 2.7, 3.15, 75, 2.30 )
                        ]
    cursor.executemany(insert_table,data_insert_table)
    conn.commit()
    conn.close()
