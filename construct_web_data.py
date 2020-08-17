import os, json
os.environ["PYTHONIOENCODING"] = "utf-8"

IN_DIR = "./data/web/data/"
FIELDS = [
    '#HOST_KEYWORDS_ANCHOR:', '#META_KEYWORDS:', '#DIRECT_KEYWORDS',
    '#BREAD_CRUMB:', '#BREAD_CRUMB_PARENT:', 
    '#DESC:', 
    '#BODY_LARGER:', '#BODY_TOP:', '#BODY_TEXT:', 
    '#NONBODY_TEXT:',
    '#HTML_H1:', '#HTML_H2:', '#HTML_H3:',
    '#HTML_TITLE:', '#HTML_TITLE_HEAD:', 
    '#IN_DOMAIN_ANCHOR:', '#OUT_DOMAIN_ANCHOR:', 
    '#FIRST_OUT_DOMAIN_TITLE:', '#ONLY_OUT_DOMAIN_TITLE:', '#OUT_DOMAIN_TITLE:', 
    
    '#SUBLINK_ALIAS:', "#SUBLINK_TITLE:",
    '#SITE_NAME:',
    
    '#URL_DOMAIN_ELEMENTS:', '#URL_PATH_ELEMENTS:', '#URL_PLD_ELEMENTS:', 
    '#URL_QUERY_ELEMENTS:', '#URL_SUBDOMAIN_ELEMENTS:',

    # '#QUERY_TEXT:', '#URL:', '#CLICK_COUNT',
]
def preprocess(v):
    if "\n" in v:
        v = v.split("\n")
        v = [_v for _v in v if "\t" not in _v else _v.split("\t")[1]]
        v = "\n".join("\n")
    else:
        return v
in_path_ls = [IN_DIR + in_path for in_path in sorted(os.listdir(IN_DIR))]
for in_path in in_path_ls:
    with open(in_path, "r", encoding="utf8") as fp:
        data = fp.readlines()
        for line in data:
            url, gdid, raw_content = line.strip().split("\t")
            content_dict = json.loads(raw_content)
            src_dict = {
                k:preprocess(v)
                for k, v in content_dict.items()
                if k in FIELDS
            }
            print(src_dict)
            tgt = content_dict["present_click_query_list"]\
                if "present_click_query_list" in content_dict\
                else  content_dict["click_query_list"]
            tgt = "|".join([dat.split("\t")[1] for dat in tgt.split("|")])
            print(tgt)
            exit()
