import streamlit as st

import plotly.graph_objects as go
import numpy as np

#create a list of rack types
rack_types=['A','B','C','D','E']
#specifying the dimensions and shelf count for different rack types
rack_shelf_dimensions={'A':(10,10,20),'B':(10,10,25),'C':(10,10,15),'D':(10,10,20),'E':(10,10,20)}
rack_shelf_count={'A':3,'B':3,'C':3,'D':3,'E':4}
rack_shelf_weight_limit={'A':100,'B':200,'C':300,'D':400,'E':500}

#initializing the list of racks, with the coordinates of the bottom left corner of the rack, and their types and axis
racks=[]
# generate a list of racks
for i in range(5):
    for j in range(5):
        
            rack = {
                'type': rack_types[i],
                'x': i * (20+rack_shelf_dimensions[rack_types[i]][0]),
                'y': j * (10+rack_shelf_dimensions[rack_types[i]][1]),
                
            }
            racks.append(rack)
            
            
#generate a list of shelves from the list of racks
shelves=[]
for rack in racks:
    for i in range(rack_shelf_count[rack['type']]):
        shelf = {
            'x': rack['x'],
            'y': rack['y'],
            'z': i * rack_shelf_dimensions[rack['type']][2],
            
            'rack_type': rack['type'],
            #setting initial weight of the shelf is random between 0 and maxed weight limit
            'weight': np.random.randint(0, 2),
            
        }
        shelves.append(shelf)
#mapping each shelf to a serial number
shelf_serial_number=0
for shelf in shelves:
    shelf['serial_number']=shelf_serial_number
    shelf_serial_number+=1
    
#creating the meshes for each shelf as a rectangle
meshes=[]
for shelf in shelves:
    mesh = go.Mesh3d(x=[shelf['x'], shelf['x']+rack_shelf_dimensions[shelf['rack_type']][0], shelf['x']+rack_shelf_dimensions[shelf['rack_type']][0], shelf['x'], shelf['x']],
                     y=[shelf['y'], shelf['y'], shelf['y']+rack_shelf_dimensions[shelf['rack_type']][1], shelf['y']+rack_shelf_dimensions[shelf['rack_type']][1], shelf['y']],
                     z=[shelf['z'], shelf['z'], shelf['z'], shelf['z'], shelf['z']],
                     i=[0, 0, 0, 0],
                     j=[1, 1, 2, 3],
                     k=[2, 3, 3, 2],
                     opacity=0.5,
                     color='orange',
                     #displaying shelf serial number and weight as text
                     
                        
                    
                    text=['shelf: '+str(shelf['serial_number'])+' weight: '+str(shelf['weight']), 'shelf: '+str(shelf['serial_number'])+' weight: '+str(shelf['weight']),'shelf: '+str(shelf['serial_number'])+' weight: '+str(shelf['weight']),'shelf: '+str(shelf['serial_number'])+' weight: '+str(shelf['weight'])],
                    hoverinfo='text',
                    )
    meshes.append(mesh)
   
#creating mesh for each shelf as a box in 3d, only if weight is greater than 0
for shelf in shelves:
    if(shelf['weight']>0):
        ratio=shelf['weight']/rack_shelf_weight_limit[shelf['rack_type']],
        mesh = go.Mesh3d(x=[shelf['x'], shelf['x']+rack_shelf_dimensions[shelf['rack_type']][0], shelf['x']+rack_shelf_dimensions[shelf['rack_type']][0], shelf['x'], shelf['x'], shelf['x']+rack_shelf_dimensions[shelf['rack_type']][0], shelf['x']+rack_shelf_dimensions[shelf['rack_type']][0], shelf['x']],
                        y=[shelf['y'], shelf['y'], shelf['y']+rack_shelf_dimensions[shelf['rack_type']][1], shelf['y']+rack_shelf_dimensions[shelf['rack_type']][1], shelf['y'], shelf['y'], shelf['y']+rack_shelf_dimensions[shelf['rack_type']][1], shelf['y']+rack_shelf_dimensions[shelf['rack_type']][1]],
                        z=[shelf['z']+5, shelf['z']+5, shelf['z']+5, shelf['z']+5,shelf['z']+rack_shelf_dimensions[shelf['rack_type']][2]-5,shelf['z']+rack_shelf_dimensions[shelf['rack_type']][2]-5,shelf['z']+rack_shelf_dimensions[shelf['rack_type']][2]-5,shelf['z']+rack_shelf_dimensions[shelf['rack_type']][2]-5],
                        i = [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
                        j = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
                        k = [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
                        
                        
                        #setting color based on ratio
                        color='gray',
                            
                        text=['shelf: '+str(shelf['serial_number'])+' weight: '+str(shelf['weight']), 'shelf: '+str(shelf['serial_number'])+' weight: '+str(shelf['weight']),'shelf: '+str(shelf['serial_number'])+' weight: '+str(shelf['weight']),'shelf: '+str(shelf['serial_number'])+' weight: '+str(shelf['weight']),'shelf: '+str(shelf['serial_number'])+' weight: '+str(shelf['weight']), 'shelf: '+str(shelf['serial_number'])+' weight: '+str(shelf['weight']),'shelf: '+str(shelf['serial_number'])+' weight: '+str(shelf['weight']),'shelf: '+str(shelf['serial_number'])+' weight: '+str(shelf['weight'])],
                        hoverinfo='text',
                            
                            
                        flatshading=True
                        )
        meshes.append(mesh)
#creating the meshes for each
# rack as a cuboid
# creating the meshes for each rack as a cuboid
for rack in racks:
    mesh = go.Mesh3d(
        x=[rack['x'], rack['x'] + rack_shelf_dimensions[rack['type']][0], rack['x'] + rack_shelf_dimensions[rack['type']][0], rack['x'], rack['x'], rack['x'] + rack_shelf_dimensions[rack['type']][0], rack['x'] + rack_shelf_dimensions[rack['type']][0], rack['x']],
        y=[rack['y'], rack['y'], rack['y'] + rack_shelf_dimensions[rack['type']][1], rack['y'] + rack_shelf_dimensions[rack['type']][1], rack['y'], rack['y'], rack['y'] + rack_shelf_dimensions[rack['type']][1], rack['y'] + rack_shelf_dimensions[rack['type']][1]],
        z=[-3, -3, -3, -3, -3, -3, -3, -3],
        i=[0, 0, 0, 0, 4, 4, 4, 4],
        j=[1, 1, 2, 3, 5, 5, 6, 7],
        k=[2, 3, 3, 2, 6, 7, 7, 6],
        color='red',
        hoverinfo='none',  # disable hoverinfo to prevent tooltip display
          # initially select the first point
    )
    meshes.append(mesh)
#create meshes for the support columns of each rack from top shelf to bottom chelf




#creating meshes for thin rectangles from the top shelf to the bottom shelf for each rack
# for rack in racks:
#     mesh=go.Mesh3d(x=[rack['x'], rack['x']+rack_shelf_dimensions[rack['type']][0], rack['x']+rack_shelf_dimensions[rack['type']][0], rack['x'],rack['x'], rack['x']+rack_shelf_dimensions[rack['type']][0], rack['x']+rack_shelf_dimensions[rack['type']][0], rack['x']],
#                    y=[rack['y'], rack['y'], rack['y']+rack_shelf_dimensions[rack['type']][1], rack['y']+rack_shelf_dimensions[rack['type']][1],rack['y'], rack['y'], rack['y']+rack_shelf_dimensions[rack['type']][1], rack['y']+rack_shelf_dimensions[rack['type']][1]],
#                    z=[0, 0, 0, 0, 0,0,0,0],
#                   i=[0, 0, 0, 0, 4, 4, 4, 4],
#                     j=[1, 1, 2, 3, 5, 5, 6, 7],
#                     k=[2, 3, 3, 2, 6, 7, 7, 6],
#                    color='red'
#                   )
#     meshes.append(mesh)


#creating the layout for the plot,but making it not clickable
# layout = go.Layout(
#     scene=dict(
#         xaxis=dict(range=[0, 50], autorange=True, showticklabels=False),
#         yaxis=dict(range=[0, 50], autorange=True, showticklabels=False),
#         zaxis=dict(range=[0, 100], autorange=True, showticklabels=False),
#     )
# )
# # layout = go.Layout(
#     scene=dict(
#         xaxis=dict(range=[0, 50], autorange=True),
#         yaxis=dict(range=[0, 50], autorange=True),
#         zaxis=dict(range=[0, 100], autorange=True),
#     )
# )

#creating the figure
fig = go.Figure(data=meshes+ [mesh])
#st.write(fig)
#plotting the figure to streamlit
st.plotly_chart(fig)
#st.plotly_chart(fig,axis=dict(visible=False))

#show a list of all shelves and their current weights
#st.write(shelves)
#create a form to request the user to input the shelf serial number and the weight to be added
form = st.form(key='my_form')
shelf_serial_number = form.text_input(label='Enter the shelf serial number')
weight = form.text_input(label='Enter the weight')
submit = form.form_submit_button(label='Submit')
#when the form is submitted, increase the weight of the shelf with the serial number entered by the user
if submit:
    #check if values are valid integers
    if not shelf_serial_number.isdigit() or not weight.isdigit():
        st.write('Please enter valid integers')
    else:
        
        for shelf in shelves:
            if shelf['serial_number']==int(shelf_serial_number):
                if shelf['weight']+int(weight)>rack_shelf_weight_limit[shelf['rack_type']]:
                    st.write('The weight exceeds the limit')
                else:
                    shelf['weight']+=int(weight)
                #update the text of the shelf to display the new weight
                    for mesh in meshes[0:len(shelves)]:
                        #st.write(mesh['text'][0].split(' ')[1])
                        #st.write(shelf_serial_number)
                        if mesh['text'][0].split(' ')[1]==shelf_serial_number:
                            mesh['text']=['shelf: '+str(shelf['serial_number'])+' weight: '+str(shelf['weight']), 'shelf: '+str(shelf['serial_number'])+' weight: '+str(shelf['weight']),'shelf: '+str(shelf['serial_number'])+' weight: '+str(shelf['weight']),'shelf: '+str(shelf['serial_number'])+' weight: '+str(shelf['weight'])]
        #update the figure with the new weights
                    fig = go.Figure(data=meshes+ [mesh])
                    #refres the initial plotly plot
                    st.plotly_chart(fig, config={'displayModeBar': False})
        #refresh the webpaage
                    
                    
        
        #st.plotly_chart(fig, config={'displayModeBar': False})
        
        #st.write(fig)
        #st.plotly_chart(fig,axis=dict(visible=False))
        #show the updated list of shelves
        #st.write(shelves)
        

