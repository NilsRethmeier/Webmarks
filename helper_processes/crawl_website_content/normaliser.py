
# TODO: What happens if it is just gibberish? Try except + errorlog + timestamp
def build_identifier(domain):
    #print (domain)
    domain_base=domain
    if domain.endswith("/")==False:
        domain_base=domain_base+"/"

    #print (domain_base)
    domain_base=domain.split("/",3)
    #print (domain_base)

    if domain_base[0]=="http:":
        domain_full=domain_base[0]+"//"+domain_base[2]+"/"
        domain_allowed=domain_base[2].replace("www.","")
        domain_identifier=domain_allowed.replace(".","_")
        domain_identifier=domain_identifier.replace("/","")


    elif domain_base[0]=="https:":
        domain_full=domain_base[0]+"//"+domain_base[2]+"/"
        domain_allowed=domain_base[2].replace("www.","")
        domain_identifier=domain_allowed.replace(".","_")
        domain_identifier=domain_identifier.replace("/","")


    elif domain_base[0].startswith("www")==True:
        domain_full="http://"+domain_base[0]+"/"
        domain_allowed=domain_base[0].replace("www.","")
        domain_identifier=domain_allowed.replace(".","_")
        domain_identifier=domain_identifier.replace("/","")


    else:
        domain_full="http://www."+domain_base[0]+"/"
        domain_allowed=domain_base[0]
        domain_identifier=domain_allowed.replace(".","_")
        domain_identifier=domain_identifier.replace("/","")

    #print (domain_full)
    #print (domain_allowed)
    #print (domain_identifier)
    #print ("\n")

    return (domain_full, domain_allowed,domain_identifier)


#### TEST VARIATIONS:
# build_identifier("https://www.scientificbeekeeping.com/")
# build_identifier("http://www.scientificbeekeeping.com/")
# build_identifier("http://www.scientificbeekeeping.com/a-review-of-dr-lus-paper-on-neonics-in-massachusetts/")
# build_identifier("www.scientificbeekeeping.com/a-review-of-dr-lus-paper-on-neonics-in-massachusetts/")
# build_identifier("www.scientificbeekeeping.com/")
#build_identifier("scientificbeekeeping.com")
#build_identifier("scientificbeekeeping.com/")
#build_identifier("http://www.test.de")





def remove_querystrings(url):
    url_wo_querystring=url.split("?",1)[0]
    #print (url_wo_querystring)

    return url_wo_querystring



#### TEST VARIATIONS:
# remove_querystrings("https://www.scientificbeekeeping.com/?url=TESTTEST")
# remove_querystrings("http://www.scientificbeekeeping.com/?url=TESTTEST")
# remove_querystrings("http://www.scientificbeekeeping.com/a-review-of-dr-lus-paper-on-neonics-in-massachusetts/?url=TESTTEST")
# remove_querystrings("www.scientificbeekeeping.com/a-review-of-dr-lus-paper-on-neonics-in-massachusetts/?url=TESTTEST")
# remove_querystrings("www.scientificbeekeeping.com/?url=TESTTEST")
# remove_querystrings("scientificbeekeeping.com")
# remove_querystrings("scientificbeekeeping.com/?url=TESTTEST")





