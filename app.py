from flask import Flask, render_template, request

app = Flask(__name__, template_folder="/home/keouck/Documents/tilde-landing-page/")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user_inputs', methods=['POST'])
def user_inputs():
    output = f'''
        {request.form.get("user_command")}
        <form action="user_inputs" method="post">
    <div id="container">
        <output></output>
        <div id="input-line" class="input-line">[user@keouck ~]$
          <div class="prompt"></div><div><input class="cmdline" autofocus required="required" name="user_command"/></div> <input type="submit" hidden/>
        </div>
      </div><br>
    </form>

    {{ output|safe }}
    '''
    return render_template('index.html', output=output)

if __name__ == "__main__":
    app.run(debug=True)
