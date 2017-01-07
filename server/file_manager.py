import os 

def _log(s):
    print 'FILE: %s' % s

class FileManager(object):
    def __init__(self, dir_name):
        self._dir_name = dir_name

    def upload_to_server(self, file_name, content):
        if os.path.exist(os.path.join(self._dir_mame, file_name)):
            try:
                _log('exist duplicate file name <%s>' % file_name)
                duplicate_index = 0
                while os.path.exist(os.path.join(self._dir_mame, '%d.%s' % (duplicate_index, file_name))):
                    duplicate_index += 1
                file_name = '%d.%s' % (duplicate_index, file_name)
                with open(os.path.join(self._dir_name, file_name), 'w') as f:
                    f.write(content)
                _log('Add duplicate_index to the file_name <%s> and upload success' % file_name)
                return file_name
            except:
                return None
        else:
            try:
                with open(os.path.join(self._dir_name, file_name), 'w') as f:
                    f.write(content)
                _log('<%s> upload success' % file_name)
                return file_name
            except:
                return None

    def get_from_server(self, file_name):
        try:
            with open(os.path.join(self._dir_name, file_name), 'r') as f:
                content = f.read()
            _log('<%s> download success' % file_name)
            return content
        except:
            return None
