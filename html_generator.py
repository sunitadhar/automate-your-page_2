head= ['1. Computer', '2. Computer Program', '3. Programming Language','4. Phython', '5 Python Grammer', 
       '6. Variables in Python', '7. Strings in Python']

concepts = [['Computer',' Most machines are designed to do few things but computers cannot do anything on its'+
            'own unless you write programs to instruct them to do many things. Computer is an electronic'+
            'device for storing and processing data according to instructions given to it in a program.'],
            ['Computer Program',' Program is a set of instructions that programmers write to instruct computers'+
             'to what to do. Some examples are Web browsers, games, apps, and so on.'],
            ['Programming Language',' Programming Language like Python is a language that programmers use to'+
             'write set of instructions that in turn instructs the computer to what to do.'],
            ['Python',' Python is an programming language. It converts the code into the language computer'+ 
            ' understands and executes.'],
            ['Python Grammar',' Python Grammar are set of rules that programmers follow while writing the code.'+
             'It is the same as we have English grammar rules. In Python, we have expression,'+
             'followed by operation, followed by expression. Expression can be replaced either by another'+
             'expression or numbers (0,1,...). Operation is what kind of operations we want to do with those'+
             'numbers. In short, we have to follow set of rules while coding so that computer can interpret'+
             'and execute correctly.'],
            ['Variables in Python',' We use variables to give names to values. For example if speed_of_car'+
             'is a variable with a value of 20 then the following code would print out 2000:'+
             '   print 100 * speed_of_car'],
            ['Strings in Python', 'String is a sequence of characters in a quote or quotes.  For example:'+
             ' name = "Dave"'+ 
             ' print "Hello " + name'+ 
            '  The result will be Hello Dave']]

 
def contents(headings):
	html_head = ''
	for contents_heading in headings:
		html_head =  html_head + '''
		''' +  contents_heading
	html_head_1 = '''
  <div class="tableofcontents">
	''' + html_head
	html_head_2 = '''

  </div>'''
	full_head = html_head_1 + html_head_2
	return full_head

def generate_concept_html(def_concept):
    def_title = def_concept[0]
    def_description = def_concept[1]
    html_concept_1 = '''
	<div class = "def_title">
	''' + def_title
    html_concept_2 = '''
	</div>
       	<div class = "def_description">
	''' + def_description
    html_concept_3 = '''
	</div>
    '''
    html_all = html_concept_1 + html_concept_2 + html_concept_3
    return html_all

def generate_all_html(text):
	all_html = '''
   <div class = "lesson4">
   '''
	counter = 0
	for title_descrip in text:
		concept = text[counter]
		html = generate_concept_html(concept)
		all_html = all_html + html
		counter = counter + 1
        all_html = all_html + '''
    </div>
    '''
	return all_html

print contents(head) 
print generate_all_html(concepts)