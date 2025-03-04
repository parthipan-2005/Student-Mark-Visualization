import pandas as pd
import streamlit as st
import plotly.express as px  
import base64
import plotly.graph_objects as go
from io import StringIO, BytesIO 
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Excel Plotter', layout='centered')

#home page
options = ["GRADE ANALYSIS", "MARK ANALYSIS"]
selected_option = st.selectbox("Select an option", options)

st.write("You selected:", selected_option)

#grade analysis
if selected_option=="GRADE ANALYSIS":

    st.title('Markviz 📈')
    st.subheader('Feed me with your Excel file')

    # Load the Excel file into a Pandas DataFrame
    file = st.file_uploader('Upload a file', type='xlsx')

    # If a file is uploaded, read it into a DataFrame
    if file is not None:
        df = pd.read_excel(file, sheet_name=None)

        # Concatenate all sheets into a single DataFrame
        df = pd.concat(df.values())

        # Calculate the number of students in each grade for each department
        grade_counts = df.groupby(['Department', 'grades'])['name'].count().reset_index()
        grade_counts = grade_counts.rename(columns={'name': 'Count'})

        # Calculate the number of students in each grades
        grades_counts = df['grades'].value_counts()

        # Calculate the number of high grades students in each department
        dept_high_grades_counts = df[df['grades'].isin(['A', 'A+'])].groupby('Department')['name'].count()

        # Calculate the average grades for each department
        dept_avg_grades = df.groupby('Department')['grades'].apply(lambda x: x.map({'O': 10, 'A+': 9, 'A': 8, 'B+': 7, 'B': 6, 'C': 5}).mean())

        # Create a bar chart showing the grades counts
        fig1 = px.bar(x=grades_counts.index, y=grades_counts.values, labels={'x': 'Grades', 'y': 'Number of Students'},
                      title='<b>Number of Students in Each Grade</b>')

        # Create a bar chart showing the high grades student counts by department
        fig2 = px.bar(x=dept_high_grades_counts.index, y=dept_high_grades_counts.values, labels={'x': 'Department', 'y': 'Number of High Grades Students'},
                      title='<b>Number of High Grades Students in Each Department</b>')

        # Create a bar chart showing the average grades for each department
        fig3 = px.bar(x=dept_avg_grades.index, y=dept_avg_grades.values, labels={'x': 'Department', 'y': 'Average Grades'},
                      title='<b>Average Grades for Each Department</b>')

        # Create a dropdown for selecting a department
        department_options = ['All Departments'] + sorted(df['Department'].unique())
        selected_department = st.sidebar.selectbox('Select a department', department_options)

        if selected_department == 'All Departments':
            # Show all grade distributions
            fig4 = px.histogram(df, x='grades', color='Department', barmode='group', 
                                 category_orders={'grades': ['O', 'A+', 'A', 'B+', 'B', 'C']},
                                 title='<b>Grade Distribution for All Departments</b>')
            st.plotly_chart(fig4)
             # Display the charts in Streamlit
            st.plotly_chart(fig1)
            st.plotly_chart(fig2)
            st.plotly_chart(fig3)


        else:

            selected_dept_data = df[df['Department'] == selected_department]
            fig4 = px.histogram(selected_dept_data, x='grades', 
                                 category_orders={'grades': ['O', 'A+', 'A', 'B+', 'B', 'C']},
                                 title=f'<b>Grade Distribution for {selected_department}</b>')
            st.plotly_chart(fig4)

   
if selected_option=="MARK ANALYSIS":
    


    
    with st.sidebar:
        selected_option = option_menu(
            menu_title=None,
            options=["Home","Department OF Computer Science","Department OF Computer Science and Buisness System ","Department OF AIDS","Department OF Mechanical","Department OF ECE","Department OF EEE","Department OF Civil"],
            
        )


    # HOME PAGE SECTION

    if selected_option=="Home":


    #main page
        st.title('Markviz 📈')
        st.subheader('Feed me with your Excel file')

        #uploding the file need to be visualized
        
        uploaded_file = st.file_uploader('Choose a XLSX file', type='xlsx')
        if uploaded_file:
            st.markdown('---')
            df3 = pd.read_excel(uploaded_file, engine='openpyxl')
            # st.dataframe(df3)

            
            a=pd.read_excel(uploaded_file, engine='openpyxl',sheet_name="CSBS")
            b=pd.read_excel(uploaded_file, engine='openpyxl',sheet_name="AIDS")
            c=pd.read_excel(uploaded_file, engine='openpyxl',sheet_name="CSE")
            d=pd.read_excel(uploaded_file, engine='openpyxl',sheet_name="CIVIL")
            e=pd.read_excel(uploaded_file, engine='openpyxl',sheet_name="EEE")
            f=pd.read_excel(uploaded_file, engine='openpyxl',sheet_name="ECE")
            g=pd.read_excel(uploaded_file, engine='openpyxl',sheet_name="MECH")
            H=pd.read_excel(uploaded_file, engine='openpyxl',sheet_name="ALL")
            # st.write("DEPARTMENT OF COMPUTER SCIENCE AND BUISNEESS SYSTEM")
            # st.dataframe(a)
            # st.dataframe(b)
            # st.dataframe(c)
            # st.dataframe(d)
            # st.dataframe(e)
            # st.dataframe(f)
            # st.dataframe(g)

            # python mean values

            dia1=px.bar(
                a,
                x=["CSBS","AIDS","CSE","CIVIL","EEE","ECE","MECH"],
                y=[a['python'].mean(),b['python'].mean(),c['python'].mean(),d['python'].mean(),e['python'].mean(),f['python'].mean(),g['python'].mean()],
                title=f'<b>Department Average in python</b>'
            )
            st.plotly_chart(dia1)

            # mathematics


            dia2=px.bar(
                a,
                x=["CSBS","AIDS","CSE","CIVIL","EEE","ECE","MECH"],
                y=[a['mathematics'].mean(),b['mathematics'].mean(),c['mathematics'].mean(),d['mathematics'].mean(),e['mathematics'].mean(),f['mathematics'].mean(),g['mathematics'].mean()],
                title=f'<b>Department Average in mathematics </b>'
            )
            st.plotly_chart(dia2)



            dia3=px.bar(
                a,
                x=["CSBS","AIDS","CSE","CIVIL","EEE","ECE","MECH"],
                y=[a['english'].mean(),b['english'].mean(),c['english'].mean(),d['english'].mean(),e['english'].mean(),f['english'].mean(),g['english'].mean()],
                title=f'<b>Department Average in english</b>'
            )
            st.plotly_chart(dia3)


            dia4=px.bar(
                a,
                x=["CSBS","AIDS","CSE","CIVIL","EEE","ECE","MECH"],
                y=[a['chemistry'].mean(),b['chemistry'].mean(),c['chemistry'].mean(),d['chemistry'].mean(),e['chemistry'].mean(),f['chemistry'].mean(),g['chemistry'].mean()],
                title=f'<b>Department Average in chemistry</b>'
            )
            st.plotly_chart(dia4)


            dia5=px.bar(
                a,
                x=["CSBS","AIDS","CSE","CIVIL","EEE","ECE","MECH"],
                y=[a['physics'].mean(),b['physics'].mean(),c['physics'].mean(),d['physics'].mean(),e['physics'].mean(),f['physics'].mean(),g['physics'].mean()],
                title=f'<b>Department Average in physics</b>'
            )
            st.plotly_chart(dia5)

            st.write("MARKS VISULIZATION OF AN INDIVIDUAL")
            user_name = st.text_input("ENTER THE NAME OF THE STUDENT :")

            H.set_index("name", inplace = True)
            if user_name:
                all=px.line(
                    H,
                    x=['Python','Mathematics','English','Chemistry','Physics'],
                    y=[H.at[user_name,'python'],H.at[user_name,'mathematics'] ,H.at[user_name,'english'],H.at[user_name,'chemistry'],H.at[user_name,'physics']],
                    title=f'<b>MARKS OF THE STUDENT YOU HAVE ENTERED </b>',
                )
                st.plotly_chart(all)



    # DEPARTMENT OF COMPUTER AND SCIENCE
    if selected_option=="Department OF Computer Science":
    
        
        uploaded_file1= st.file_uploader('Choose a XLSX file', type='xlsx')
        if uploaded_file1:
            st.markdown('---')
            df = pd.read_excel(uploaded_file1, engine='openpyxl',sheet_name='CSE')
            st.write("NAME LIST OF THE STUDENTS")
            st.dataframe(df)
            #bar chart three
            st.write("")

        

            fig2=px.bar(
                df,
                x=['PYTHON','MATHEMATICS','ENGLISH','CHEMISTRY','PHYSICS'],
                y=[df["python"].mean(),df["mathematics"].mean(),df["english"].mean(),df["chemistry"].mean(),df["physics"].mean()],
                title=f'<b> SUBJECT AVERAGE OF THE STUDENTS</b>',
            
            )
            st.plotly_chart(fig2)


        
        # line chart 
            fig3=px.line(
                df,
                x=['Python','Mathematics','English','Chemistry','Physics'],
                y=[df['python'].max(),df['mathematics'].max(),df['english'].max(),df['chemistry'].max(),df['physics'].max()],
                
                title=f'<b> HIGHEST MARKS IN EACH SUBJECTS</b>',
                
            )
            st.plotly_chart(fig3)

        # printing top five students name and their marks

            st.markdown('---')
            st.write(" TOP 5 STUDENTS WITH HIGHEST AVERAGE MARKS IN THEIR SUBJECTS")
            st.markdown('---')
            df.set_index("name", inplace = True)
            top_five=pd.DataFrame(df['average'].nlargest(n=5))
            st.dataframe(top_five)
        


        
        #user input and printing a bar chart with the name entered
        



    if selected_option=="Department OF Computer Science and Buisness System ":
        uploaded_file2 = st.file_uploader('Choose a XLSX file', type='xlsx')
        if uploaded_file2:
            st.markdown('---')
            df1 = pd.read_excel(uploaded_file2, engine='openpyxl',sheet_name='CSBS')
            st.dataframe(df1)
            fig2=px.bar(
                df1,
                x=['PYTHON','MATHEMATICS','ENGLISH','CHEMISTRY','PHYSICS'],
                y=[df1["python"].mean(),df1["mathematics"].mean(),df1["english"].mean(),df1["chemistry"].mean(),df1["physics"].mean()],
                title=f'<b> SUBJECT AVERAGE OF THE STUDENTS</b>',
            
            )
            st.plotly_chart(fig2)
        
        # line chart 
            fig3=px.line(
                df1,
                x=['Python','Mathematics','English','Chemistry','Physics'],
                y=[df1['python'].max(),df1['mathematics'].max(),df1['english'].max(),df1['chemistry'].max(),df1['physics'].max()],
                title=f'<b> HIGHEST MARKS IN EACH SUBJECTS</b>',
                
            )
            st.plotly_chart(fig3)

        # printing top five students name and their marks

            st.markdown('---')
            st.write(" TOP 5 STUDENTS WITH HIGHEST AVERAGE MARKS IN THEIR SUBJECTS")
            st.markdown('---')
            df1.set_index("name", inplace = True)
            top_five=pd.DataFrame(df1['average'].nlargest(n=5))
            st.dataframe(top_five)
        


        
        #user input and printing a bar chart with the name entered
        
    if selected_option=="Department OF AIDS":
        uploaded_file3 = st.file_uploader('Choose a XLSX file', type='xlsx')
        if uploaded_file3:
            st.markdown('---')
            df2= pd.read_excel(uploaded_file3, engine='openpyxl',sheet_name='AIDS')
            st.dataframe(df2)
            fig2=px.bar(
                df2,
                x=['PYTHON','MATHEMATICS','ENGLISH','CHEMISTRY','PHYSICS'],
                y=[df2["python"].mean(),df2["mathematics"].mean(),df2["english"].mean(),df2["chemistry"].mean(),df2["physics"].mean()],
                title=f'<b> SUBJECT AVERAGE OF THE STUDENTS</b>',
            
            )
            st.plotly_chart(fig2)
        
        # line chart 
            fig3=px.line(
                df2,
                x=['Python','Mathematics','English','Chemistry','Physics'],
                y=[df2['python'].max(),df2['mathematics'].max(),df2['english'].max(),df2['chemistry'].max(),df2['physics'].max()],
                title=f'<b> HIGHEST MARKS IN EACH SUBJECTS</b>',
                
            )
            st.plotly_chart(fig3)

        # printing top five students name and their marks

            st.markdown('---')
            st.write(" TOP 5 STUDENTS WITH HIGHEST AVERAGE MARKS IN THEIR SUBJECTS")
            st.markdown('---')
            df2.set_index("name", inplace = True)
            top_five=pd.DataFrame(df2['average'].nlargest(n=5))
            st.dataframe(top_five)
        


        
        #user input and printing a bar chart with the name entered
        
    if selected_option=="Department OF Mechanical":
        uploaded_file = st.file_uploader('Choose a XLSX file', type='xlsx')
        if uploaded_file:
            st.markdown('---')
            df4 = pd.read_excel(uploaded_file, engine='openpyxl',sheet_name="MECH")
            st.dataframe(df4)
            fig2=px.bar(
                df4,
                x=['PYTHON','MATHEMATICS','ENGLISH','CHEMISTRY','PHYSICS'],
                y=[df4["python"].mean(),df4["mathematics"].mean(),df4["english"].mean(),df4["chemistry"].mean(),df4["physics"].mean()],
                title=f'<b> SUBJECT AVERAGE OF THE STUDENTS</b>',
            
            )
            st.plotly_chart(fig2)
        
        # line chart 
            fig3=px.line(
                df4,
                x=['Python','Mathematics','English','Chemistry','Physics'],
                y=[df4['python'].max(),df4['mathematics'].max(),df4['english'].max(),df4['chemistry'].max(),df4['physics'].max()],
                title=f'<b> HIGHEST MARKS IN EACH SUBJECTS</b>',
                
            )
            st.plotly_chart(fig3)

        # printing top five students name and their marks

            st.markdown('---')
            st.write(" TOP 5 STUDENTS WITH HIGHEST AVERAGE MARKS IN THEIR SUBJECTS")
            st.markdown('---')
            df4.set_index("name", inplace = True)
            top_five=pd.DataFrame(df4['average'].nlargest(n=5))
            st.dataframe(top_five)
            
    if selected_option=="Department OF ECE":
        uploaded_file = st.file_uploader('Choose a XLSX file', type='xlsx')
        if uploaded_file:
            st.markdown('---')
            df5 = pd.read_excel(uploaded_file, engine='openpyxl',sheet_name="ECE")
            st.dataframe(df5)
            fig2=px.bar(
                df5,
                x=['PYTHON','MATHEMATICS','ENGLISH','CHEMISTRY','PHYSICS'],
                y=[df5["python"].mean(),df5["mathematics"].mean(),df5["english"].mean(),df5["chemistry"].mean(),df5["physics"].mean()],
                title=f'<b> SUBJECT AVERAGE OF THE STUDENTS</b>',
            
            )
            st.plotly_chart(fig2)
        
        # line chart 
            fig3=px.line(
                df5,
                x=['Python','Mathematics','English','Chemistry','Physics'],
                y=[df5['python'].max(),df5['mathematics'].max(),df5['english'].max(),df5['chemistry'].max(),df5['physics'].max()],
                title=f'<b> HIGHEST MARKS IN EACH SUBJECTS</b>',
                
            )
            st.plotly_chart(fig3)

        # printing top five students name and their marks

            st.markdown('---')
            st.write(" TOP 5 STUDENTS WITH HIGHEST AVERAGE MARKS IN THEIR SUBJECTS")
            st.markdown('---')
            df5.set_index("name", inplace = True)
            top_five=pd.DataFrame(df5['average'].nlargest(n=5))
            st.dataframe(top_five)

    if selected_option=="Department OF EEE":
        uploaded_file = st.file_uploader('Choose a XLSX file', type='xlsx')
        if uploaded_file:
            st.markdown('---')
            df6 = pd.read_excel(uploaded_file, engine='openpyxl',sheet_name="EEE")
            st.dataframe(df6)
            fig2=px.bar(
                df6,
                x=['PYTHON','MATHEMATICS','ENGLISH','CHEMISTRY','PHYSICS'],
                y=[df6["python"].mean(),df6["mathematics"].mean(),df6["english"].mean(),df6["chemistry"].mean(),df6["physics"].mean()],
                title=f'<b> SUBJECT AVERAGE OF THE STUDENTS</b>',
            
            )
            st.plotly_chart(fig2)
        
        # line chart 
            fig3=px.line(
                df6,
                x=['Python','Mathematics','English','Chemistry','Physics'],
                y=[df6['python'].max(),df6['mathematics'].max(),df6['english'].max(),df6['chemistry'].max(),df6['physics'].max()],
                title=f'<b> HIGHEST MARKS IN EACH SUBJECTS</b>',
                
            )
            st.plotly_chart(fig3)

        # printing top five students name and their marks

            st.markdown('---')
            st.write(" TOP 5 STUDENTS WITH HIGHEST AVERAGE MARKS IN THEIR SUBJECTS")
            st.markdown('---')
            df6.set_index("name", inplace = True)
            top_five=pd.DataFrame(df6['average'].nlargest(n=5))
            st.dataframe(top_five)





    if selected_option=="Department OF Civil":
        uploaded_file = st.file_uploader('Choose a XLSX file', type='xlsx')
        if uploaded_file:
            st.markdown('---')
            df7 = pd.read_excel(uploaded_file, engine='openpyxl',sheet_name="CIVIL")
            st.dataframe(df7)
            fig2=px.bar(
                df7,
                x=['PYTHON','MATHEMATICS','ENGLISH','CHEMISTRY','PHYSICS'],
                y=[df7["python"].mean(),df7["mathematics"].mean(),df7["english"].mean(),df7["chemistry"].mean(),df7["physics"].mean()],
                title=f'<b> SUBJECT AVERAGE OF THE STUDENTS</b>',
            
            )
            st.plotly_chart(fig2)
        
        # line chart 
            fig3=px.line(
                df7,
                x=['Python','Mathematics','English','Chemistry','Physics'],
                y=[df7['python'].max(),df7['mathematics'].max(),df7['english'].max(),df7['chemistry'].max(),df7['physics'].max()],
                title=f'<b> HIGHEST MARKS IN EACH SUBJECTS</b>',
                
            )

            
            st.plotly_chart(fig3)

        # printing top five students name and their marks

            st.markdown('---')
            st.write(" TOP 5 STUDENTS WITH HIGHEST AVERAGE MARKS IN THEIR SUBJECTS")
            st.markdown('---')
            df7.set_index("name", inplace = True)
            top_five=pd.DataFrame(df7['average'].nlargest(n=5))
            st.dataframe(top_five)
