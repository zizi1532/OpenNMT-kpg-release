import os, json, numpy as np
os.environ["PYTHONIOENCODING"] = "utf-8"

IN_DIR = "./data/web/data/"
FIELDS = [
    '#HOST_KEYWORDS_ANCHOR:', '#META_KEYWORDS:', 
    # '#DIRECT_KEYWORDS', #* 값이 없음
    '#BREAD_CRUMB:', 
    '#BREAD_CRUMB_PARENT:', 
    '#DESC:', 
    '#BODY_LARGER:', '#BODY_TOP:', '#BODY_TEXT:', 
    '#NONBODY_TEXT:',
    '#HTML_H1:', '#HTML_H2:', '#HTML_H3:',
    '#HTML_TITLE:', '#HTML_TITLE_HEAD:', 
    '#IN_DOMAIN_ANCHOR:', '#OUT_DOMAIN_ANCHOR:', 
    '#FIRST_OUT_DOMAIN_TITLE:', '#ONLY_OUT_DOMAIN_TITLE:', '#OUT_DOMAIN_TITLE:', 
    
    # '#SUBLINK_ALIAS:', "#SUBLINK_TITLE:", #* 값이 없음
    
    '#SITE_NAME:',
    
    #* precision, recall 이 너무 낮음
    # '#URL_PATH_ELEMENTS:', 
    # '#URL_DOMAIN_ELEMENTS:', '#URL_PLD_ELEMENTS:', '#URL_QUERY_ELEMENTS:', '#URL_SUBDOMAIN_ELEMENTS:', 

    # '#QUERY_TEXT:', '#URL:', '#CLICK_COUNT',
]
# * seq (a sequence of words), 
# * multi-seq (sequences of words), 
# * list (words without sequential order)
FIELD_TO_type = {
    "#HOST_KEYWORDS_ANCHOR:":"multi-seq",
    "#META_KEYWORDS:":"list",
    "#BREAD_CRUMB:":"seq",
    "#BREAD_CRUMB_PARENT:":"seq",
    "#DESC:":"seq",
    "#BODY_LARGER:": "seq",
    "#BODY_TOP:":"seq",
    "#BODY_TEXT:":"seq",
    "#NONBODY_TEXT:":"seq",
    "#HTML_H1:":"seq",
    "#HTML_H2:":"seq",
    "#HTML_H3:":"seq",
    "#HTML_TITLE:":"seq",
    "#HTML_TITLE_HEAD:":"list",
    "#IN_DOMAIN_ANCHOR:":"multi-seq",
    "#OUT_DOMAIN_ANCHOR:":"multi-seq",
    "#FIRST_OUT_DOMAIN_TITLE:":"multi-seq",
    "#ONLY_OUT_DOMAIN_TITLE:":"multi-seq",
    "#OUT_DOMAIN_TITLE:":"multi-seq",
    "#SITE_NAME:":"seq",
}
def preprocess(v):
    if "\n" in v:
        v = v.split("\n")
        v = [_v if "\t" not in _v else _v.split("\t")[1] for _v in v]
        v = "\n".join("\n")
        return v if v.strip() else None
    else:
        v = v if "\t" not in v else v.split("\t")[1]
        return v if v.strip() else None
in_path_ls = [IN_DIR + in_path for in_path in sorted(os.listdir(IN_DIR))]
current_file_path = os.path.abspath(__file__)
dirname = os.path.dirname(current_file_path)+"/data/web"
src_json_data = []
tgt_json_data = []
for in_path in in_path_ls:
    with open(in_path, "r", encoding="utf8") as fp_read:
        data = fp_read.readlines()
        for line in data:
            url, gdid, raw_content = line.strip().split("\t")
            content_dict = json.loads(raw_content)
            src_dict = {
                k:preprocess(v)
                for k, v in content_dict.items()
                if k in FIELDS
            }
            tgt = content_dict["present_click_query_list"]\
                if "present_click_query_list" in content_dict\
                else  content_dict["click_query_list"]
            tgt = [dat.split("\t")[1] for dat in tgt.split("|")]
            src_json = json.dumps(src_dict)
            tgt_json = json.dumps(tgt)
            src_json_data.append(src_json+"\n")
            tgt_json_data.append(tgt_json+"\n")

shuffle_index = np.random.permutation(len(src_json_data))
n_valid, n_test = 1000, 1000
n_train = len(shuffle_index) -n_valid -n_test
idx_train = shuffle_index[:n_train]
idx_valid = shuffle_index[n_train:n_train+n_valid]
idx_test = shuffle_index[n_train+n_valid:]
for data_type, idx_ls in [
    ("valid", idx_valid),
    ("test", idx_test),
    ("train", idx_train)
]:
    src_path = "{}/src-{}.txt".format(dirname, data_type)
    tgt_path = "{}/tgt-{}.txt".format(dirname, data_type)
    with open(src_path, "w", encoding="utf8") as src_write\
        ,open(tgt_path, "w", encoding="utf8") as tgt_write :
        for idx in idx_ls:
            src_write.write(src_json_data[idx])
            tgt_write.write(tgt_json_data[idx])
"""
for in_path in in_path_ls:
    basename = os.path.basename(in_path)
    src_out_path = "{}/{}-src.txt".format(dirname, basename)
    tgt_out_path = "{}/{}-tgt.txt".format(dirname, basename)
    with open(in_path, "r", encoding="utf8") as fp_read, \
        open(src_out_path, "w", encoding="utf8") as fp_write_src,\
        open(tgt_out_path, "w", encoding="utf8") as fp_write_tgt:
        data = fp_read.readlines()
        for line in data:
            url, gdid, raw_content = line.strip().split("\t")
            content_dict = json.loads(raw_content)
            src_dict = {
                k:preprocess(v)
                for k, v in content_dict.items()
                if k in FIELDS
            }
            tgt = content_dict["present_click_query_list"]\
                if "present_click_query_list" in content_dict\
                else  content_dict["click_query_list"]
            tgt = [dat.split("\t")[1] for dat in tgt.split("|")]
            src_json = json.dumps(src_dict)
            tgt_json = json.dumps(tgt)
            fp_write_src.write(src_json+"\n")
            fp_write_tgt.write(tgt_json+"\n")
"""         
