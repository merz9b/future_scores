
from jinja2 import Template


def render_to_html(result):
    temp = '''
    <table border="2">
        <tr>
            <th>Date</th>
            <th>SubjectName</th>
            <th>ExamScore</th>
            <th>ExamPlace</th>
        </tr>
        {% for content in result %}
        <tr>
            <td>{{content['ExamDate']}}</td>
            <td>{{content['SubjectName']}}</td>
            <td>{{content['ExamScore']}}</td>
            <td>{{content['ExamPlace']}}</td>
        </tr>
        {% endfor %}
    </table>
    '''
    templates = Template(temp)

    return templates.render(result=result)
