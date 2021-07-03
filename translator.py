import googletrans
from googletrans import Translator

def translate(query):
    trans=0
    if "french" in query:
        try :
            query=query.replace("into french","")
        except:
            query=query.replace("to french","")
        des="fr"
        
    elif "german" in query:
        try :
            query=query.replace("into german","")
        except:
            query=query.replace("to german","")
        des="de"
    
    elif "hindi" in query:
        try :
            query=query.replace("into hindi","")
        except:
            query=query.replace("to hindi","")
        des="hi"
        
    elif "english" in query:
        try :
            query=query.replace("into english","")
        except:
            query=query.replace("to english","")
        des="en"    
    
    elif "spanish" in query:
        try :
            query=query.replace("into spanish","")
        except:
            query=query.replace("to spanish","")
        des="es"
    
    elif "russian" in query:
        try :
            query=query.replace("into russian","")
        except:
            query=query.replace("to russian","")
        des="ru"
    
    elif "turkish" in query:
        try :
            query=query.replace("into turkish","")
        except:
            query=query.replace("to turkish","")
        des="tr"
    
    elif "indonesian" in query:
        try :
            query=query.replace("into indonesian","")
        except:
            query=query.replace("to indonesian","")
        des="id"
        
    elif "estonian" in query:
        try :
            query=query.replace("into estonian","")
        except:
            query=query.replace("to estonian","")
        des="et"
    
    elif "bulgarian" in query:
        try :
            query=query.replace("into bulgarian","")
        except:
            query=query.replace("to bulgarian","")
        des="bg"
    
    elif "portuguese" in query:
        try :
            query=query.replace("into portuguese","")
        except:
            query=query.replace("to portuguese","")
        des="pt"
    
    elif "urdu" in query:
        try :
            query=query.replace("into urdu","")
        except:
            query=query.replace("to urdu","")
        des="ur"
    
    elif "azerbaijani" in query:
        try :
            query=query.replace("into azerbaijani","")
        except:
            query=query.replace("to azerbaijani","")
        des="az"
    
    else:
        trans="None"
    
    if trans=="None":
        tran="Language is not available"
    else:
        sen="Hello"
        translator=Translator()
        
        translated=translator.translate(sen, dest=des, src='auto')
        tran=query +"+" + translated.text
    
    # print(query)
    return tran

# print(translate("hello into french"))


