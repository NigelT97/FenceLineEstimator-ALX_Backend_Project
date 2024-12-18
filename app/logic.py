# Logic for fencing calculations
import sqlite3
from config import DATABASE_PATH

def calculated_estimate(fence_perimeter, fence_height, perimeter_corners, fence_type,fence_wire_thickness, fence_appeture, fence_overhang_request, fence_overhang_type):
    # Get Parameters of the fence type
    Parameter_materials = parameter_type(fence_type)
    
    # Number of steelworks
    Num_Post = int((fence_perimeter/Parameter_materials[0]) + perimeter_corners)
    Num_Stay = int(Num_Post + perimeter_corners)
    Num_DVs = int((fence_perimeter/Parameter_materials[1]) - (fence_perimeter/Parameter_materials[0]))
    
    # Number of Fence Rolls
    Num_Fence = int(fence_perimeter/Parameter_materials[2])
    
    # Number of wire strands
    Strands_Num = HighStrainCalculator(fence_height)
    Num_HighStrain = int((fence_perimeter*Strands_Num)/30)
    
    Num_TyingWire = int(Num_HighStrain/Strands_Num)
    
    # Overhang Calculations
    if fence_overhang_request == 'Y':
        Num_Overhang = OverhangCalc(fence_overhang_type, fence_perimeter)
    
    # Define material description and quantity
    DescrMaterial = DescriptionRequaired(fence_type, fence_height, fence_wire_thickness, fence_appeture, fence_overhang_request, fence_overhang_type)
    
    # Forming Results
    if fence_overhang_request == 'Y':
        ParameterTest = {DescrMaterial[0]: Num_Post,
                        DescrMaterial[1]: Num_Stay,
                        DescrMaterial[2]: Num_DVs,
                        DescrMaterial[3]: Num_Fence,
                        DescrMaterial[4]: Num_Overhang,
                        '2.24mm High-Strain Wire 1kg': Num_HighStrain,
                        '1.6mm Galv Wire 1kg': Num_TyingWire
                        }
        
    elif fence_overhang_request == 'N':
        ParameterTest = {DescrMaterial[0]: Num_Post,
                        DescrMaterial[1]: Num_Stay,
                        DescrMaterial[2]: Num_DVs,
                        DescrMaterial[3]: Num_Fence,
                        '2.24mm High-Strain Wire 1kg': Num_HighStrain,
                        '1.6mm Galv Wire 1kg': Num_TyingWire
                        }
      
    return ParameterTest
    
    
def parameter_type(fence_type):
    # Get Parameters of the fenec type
    if fence_type == 'diamond mesh':
        post_spacing = 45
        dv_spacing = 4.5
        fence_roll = 30
        Parameters = [post_spacing, dv_spacing, fence_roll]
        return (Parameters)
        
    elif fence_type == 'field fence':
        post_spacing = 50
        dv_spacing = 5
        fence_roll = 100
        Parameters = [post_spacing, dv_spacing, fence_roll]
        return (Parameters)
        
    elif fence_type == 'Barbed wire':
        post_spacing = 150
        dv_spacing = 10
        fence_roll = 750
        Parameters = [post_spacing, dv_spacing, fence_roll]
        return (Parameters)
        
    elif fence_type == 'Welded Mesh':
        post_spacing = 30
        dv_spacing = 3
        fence_roll = 30
        Parameters = [post_spacing, dv_spacing, fence_roll]
        return (Parameters)
        
    elif fence_type == 'anti-climp wire-wall':
        post_spacing = 3
        dv_spacing = 0
        fence_roll = 3
        Parameters = [post_spacing, dv_spacing, fence_roll]
        return (Parameters)

    else:
        return ('error')
    

def HighStrainCalculator(fence_height):
    if fence_height == 'H09' or fence_height == 'H12':
        HighStrain_strands = 2
        return HighStrain_strands
    elif fence_height == 'H15':
        HighStrain_strands = 3
        return HighStrain_strands
    elif fence_height == 'H18' or fence_height == 'H21':
        HighStrain_strands = 4
        return HighStrain_strands
    elif fence_height == 'H24' or fence_height == 'H27':
        HighStrain_strands = 5
        return HighStrain_strands
    elif fence_height == 'H30':
        HighStrain_strands = 6
        return HighStrain_strands
    
def DescriptionRequaired(fence_type, fence_height, fence_wire_thickness, fence_appeture, fence_overhang_request, fence_overhang_type):
    # Dictionaries used to define material description
    DictfenceHeight = {'H09':0.9,
                       'H12':1.2,
                       'H15':1.5,
                       'H18':1.8,
                       'H21':2.1,
                       'H24':2.4,
                       'H27':2.7,
                       'H30':3.0
                           }
    DictFenceAppeture = {'small': '50mm',
                         'moderate_small':'65mm',
                         'standard':'75mm'
                         }
    DictFenceThickness = {'L':'2mm',
                          'M':'2.5mm',
                          'H':'3.15mm',
                          'HX':'4mm'
                          }
    DictFenceOverhang = {'BWL':'2mm Barbed wire 50kg (750-800m)',
                         'FWRW':'Flatwrap razor wire 12m',
                         'CRW':'Concertina razor wire 8m',
                         'ELTRIC':'4 Strands Electric Wire'}
    
    # Determine if it has overhang or not
    if fence_overhang_request == 'Y':
        overhang = '+460mm Overhang'
    else:
        overhang =''
        DescrOverhang = ''
    
    # Define type and descruption of materials
    if fence_type == 'diamond mesh':
        DescrPost = f"{DictfenceHeight[fence_height]+0.6}m x 76 x 1.6mm Post {overhang}"
        DescrStay = f"{DictfenceHeight[fence_height]+0.6}m x 38 x 1.6mm Stay"
        DescrStad = f"{DictfenceHeight[fence_height]+0.6}m DV Standard {overhang}"
        DescrFence =  f"{DictfenceHeight[fence_height]}m x {DictFenceAppeture[fence_appeture]} x {DictFenceThickness[fence_wire_thickness]}mm Diamond-Mesh Fence (30m)"
        if fence_overhang_request == 'Y':
            DescrOverhang = f"{DictFenceOverhang[fence_overhang_type]}"
     
    if fence_type == 'field fence':
        DescrPost = f"{DictfenceHeight[fence_height]+0.6}m x 76 x 1.6mm Post {overhang}"
        DescrStay = f"{DictfenceHeight[fence_height]+0.6}m x 38 x 1.6mm Stay"
        DescrStad = f"{DictfenceHeight[fence_height]+0.6}m DV Standard {overhang}"
        DescrFence =  f"{DictfenceHeight[fence_height]}m x 3.15mm x 2.5mm x 2.24mm Field Fence (100m) "
        if fence_overhang_request == 'Y':
            DescrOverhang = f"{DictFenceOverhang[fence_overhang_type]}"
        

    if fence_type == 'Barbed wire':
        DescrPost = f"{DictfenceHeight[fence_height]+0.6}m x 76 x 1.6mm Post {overhang}"
        DescrStay = f"{DictfenceHeight[fence_height]+0.6}m x 38 x 1.6mm Stay"
        DescrStad = f"{DictfenceHeight[fence_height]+0.6}m DV Standard {overhang}"
        DescrFence =  f"{DictfenceHeight[fence_height]}m x 8 strands of {DictFenceOverhang['BWL']}"
        if fence_overhang_request == 'Y':
            DescrOverhang = f"{DictFenceOverhang[fence_overhang_type]}"
    
    if fence_type == 'Welded Mesh':
        DescrPost = f"{DictfenceHeight[fence_height]+0.6}m x Post {overhang}"
        DescrFence =  f"{DictfenceHeight[fence_height]}m x Palisade Fence"
        if fence_overhang_request == 'Y':
            DescrOverhang = f"{DictFenceOverhang[fence_overhang_type]}"
        
    if fence_type == 'anti-climb wire-wall':
        DescrPost = f"{DictfenceHeight[fence_height]+0.6}m Post {overhang}"
        DescrFence =  f"{DictfenceHeight[fence_height]}m x 3120 secure-max wire wall"
        if fence_overhang_request == 'Y':
            DescrOverhang = f"{DictFenceOverhang[fence_overhang_type]}"
    
    FullDescriptionTest = [DescrPost, DescrStay, DescrStad, DescrFence, DescrOverhang]
        
    return FullDescriptionTest

def OverhangCalc(fence_overhang_type, fence_perimeter):
    if fence_overhang_type == 'BWL':
        quantity = int((fence_perimeter * 3)/750)
    elif fence_overhang_type == 'FWRW':
        quantity = int(fence_perimeter/12)
    elif fence_overhang_type == 'CRW':
        quantity = int(fence_perimeter/8)
    elif fence_overhang_type == 'ELTRIC':
        quantity = int((fence_perimeter * 5)/30)
        
    return quantity

def cost_calculator(fence_perimeter, fence_height, fence_type, fence_overhang_request, fence_appeture, fence_thickness):
    cost = 0
    code_fence = ''
    if fence_type == 'diamond mesh':
        if fence_height == 'H09':
            if fence_appeture == 'small':
                if fence_thickness == 'L':
                    code_fence = 'DM0950L30'
                elif fence_thickness == 'M':
                    code_fence = 'DM0950M30'
                else:
                    code_fence = 'DM0950HX30'
            else:
                if fence_thickness == 'L':
                    code_fence = 'DM0975l30'
                elif fence_thickness == 'M':
                    code_fence = 'DM0975M30'
                else:
                    code_fence = 'DM0975HX30'
        elif fence_height == 'H12':
            if fence_appeture == 'small':
                if fence_thickness == 'L':
                    code_fence = 'DM1250l30'
                elif fence_thickness == 'M':
                    code_fence = 'DM1250M30'
                else:
                    code_fence = 'DM1250HX30'
            else:
                if fence_thickness == 'L':
                    code_fence = 'DM1275l30'
                elif fence_thickness == 'M':
                    code_fence = 'DM1275M30'
                else:
                    code_fence = 'DM1275HX30'
                    
        elif fence_height == 'H15':
            if fence_appeture == 'small':
                if fence_thickness == 'L':
                    code_fence = 'DM1550l30'
                elif fence_thickness == 'M':
                    code_fence = 'DM1550M30'
                else:
                    code_fence = 'DM1550HX30'
            else:
                if fence_thickness == 'L':
                    code_fence = 'DM1575l30'
                elif fence_thickness == 'M':
                    code_fence = 'DM1575M30'
                else:
                    code_fence = 'DM1575HX30'
        elif fence_height == 'H18':
            if fence_appeture == 'small':
                if fence_thickness == 'L':
                    code_fence = 'DM1850L30'
                elif fence_thickness == 'M':
                    code_fence = 'DM1850M30'
                else:
                    code_fence = 'DM1850HX30'
            else:
                if fence_thickness == 'L':
                    code_fence = 'DM1875L30'
                elif fence_thickness == 'M':
                    code_fence = 'DM1875M30'
                else:
                    code_fence = 'DM1875HX30'
        elif fence_height == 'H21':
            if fence_appeture == 'small':
                if fence_thickness == 'L':
                    code_fence = 'DM2150l30'
                elif fence_thickness == 'M':
                    code_fence = 'DM2150M30'
                else:
                    code_fence = 'DM2150HX30'
            else:
                if fence_thickness == 'L':
                    code_fence = 'DM2175l30'
                elif fence_thickness == 'M':
                    code_fence = 'DM2175M30'
                else:
                    code_fence = 'DM2175HX30'
        elif fence_height == 'H24':
            if fence_appeture == 'small':
                if fence_thickness == 'L':
                    code_fence = 'DM2450l30'
                elif fence_thickness == 'M':
                    code_fence = 'DM2450M30'
                else:
                    code_fence = 'DM2450HX30'
            else:
                if fence_thickness == 'L':
                    code_fence = 'DM2475l30'
                elif fence_thickness == 'M':
                    code_fence = 'DM2475M30'
                else:
                    code_fence = 'DM2475HX30'

    if fence_type == 'field fence':
       cost = 3.12 

    if fence_type == 'Barbed wire':
        cost = 0.28
    
    if fence_type == 'Welded Mesh':
        cost = 6.90
        
    if fence_type == 'anti-climb wire-wall':
        cost = 12.90

    if code_fence != '':
        cost = 1
        cost = retrieve_cost_value(code_fence)
        
    labour_and_material_cost = cost * float(fence_perimeter)
    
    return labour_and_material_cost
 
def retrieve_cost_value(code_fence):
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    
    query_code = "SELECT COST FROM CostTable WHERE FenceCode = ?"
                   
    cursor.execute(query_code, (code_fence,))
    
    cost_value = cursor.fetchone()
    
    if cost_value is None:
        cost_value = -34.9
        if code_fence == 'DM0950L30':
            cost_value = -1000
        conn.close()
        return cost_value
    conn.close()
    return cost_value[0]
