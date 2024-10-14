# Logic for fencing calculations

def calculated_estimate(fence_perimeter, fence_height, perimeter_corners, fence_type,fence_wire_thickness, fence_appeture, fence_overhang_request, fence_overhang_type):
    # Get Parameters of the fence type
    Parameter_materils = parameter_type(fence_type)
    
    # Number of steelworks
    Num_Post = (fence_perimeter/Parameter_materils[0]) + perimeter_corners
    Num_Stay = Num_Post + perimeter_corners
    Num_DVs = (fence_perimeter/Parameter_materils[1]) - (fence_perimeter/Parameter_materils[0])
    
    # Number of Fence Rolls
    Num_Fence = fence_perimeter/Parameter_materils[2]
    
    
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
    
    