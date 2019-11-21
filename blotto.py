#import sys; sys.argv = ['nimasasa@gmail.com',1234,2345,3456,4567]  

import requests
import argparse


def box(text, maxlen=59, symb='#'):
    n = len(text)
    str_len = int((maxlen-2-n)*1.0/2)
    
    str_len = int((maxlen-2-n)*1.0/2) if n>13 else int((maxlen-2-13)*1.0/2)
    print_statement = '''
    {}
    {} {:^13} {}
    {}
    '''.format(symb*maxlen,symb*str_len,text.strip().upper(),symb*str_len,symb*maxlen)
    print(print_statement)
    

class Blotto:
    def __init__(self):
        self.referer = "https://docs.google.com/forms/d/e/1FAIpQLSe5Q-pHaCHxU3JxMgZ9e1mKdl1W_6Cw2-K58aY2K1BKGS0ldA/viewform"
        self.responder = self.referer[:-8] + 'formResponse'
    
    def submit(self, form_data):
        user_agent = {'Referer': self.referer,
                      'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"
                     }
        
        r = requests.post(self.responder,
                          data=form_data, 
                          headers=user_agent)
        
        if r.status_code == 200:
            box('submission accepted!')
        else:
            box('submission failed, try again!')

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-e', '--email',
        help ='<Required> Your valid email',
        type = str,
        required = True
    )

    
    parser.add_argument(
        '-l','--list', 
        nargs='+', 
        help='<Required> your portfolio for each district (should sum up to 100)', 
        required=True)


    portfolio = []
    for _, value in parser.parse_args()._get_kwargs():
        if value is not None:
            portfolio.append(value)
     
    assert isinstance(portfolio[0],str), 'Email shaould be string!'
    assert len(portfolio[1])==10, 'You need to give inputs for 10 districts!'
    
    port_vals = [float(i) for i in portfolio[1]]
    
    for i in port_vals:
        assert int(i)==i, 'All enteries should be integers!'
        assert i>=0, 'All enteries should be non-negative!'
    
    assert sum(port_vals)==100, 'Enteries should sum up to 100!'
    
    labels = ['entry.2009186972',
              'entry.1253200192',
              'entry.142642749',
              'entry.1301748443',
              'entry.778113309',
              'entry.492967976',
              'entry.1655326393',
              'entry.454916203',
              'entry.613164521',
              'entry.810820827'
             ]
    
    form_data = {labels[i]:portfolio[1][i] for i in range(len(labels))}
               
    form_data['draftResponse'] = []
    form_data['pageHistory'] = '0'
    form_data['emailAddress'] = portfolio[0]
                 

    blt = Blotto()
    blt.submit(form_data)
if __name__ == '__main__':
    main()
