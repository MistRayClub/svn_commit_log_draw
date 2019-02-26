from com.mist.svn import svnCommitLog
from com.mist.svn import readExcle3
#模板路径
template_path = 'G:/data/zhoubao3.xlsx'
#输出路径
output_file_path = 'G:/data/ouput.xlsx'
logs = svnCommitLog.getSvnLog('G: && cd gjyWorkSpace/SMFdev/SMF && svn log --search ' + 'userName')
#根据模板生成excel
readExcle3.write_data(logs,template_path,output_file_path)
