class Solution:
    def simplifyPath(self, path: str) -> str:
        path_splited = path.split('/')

        ret = []
        for e in path_splited:
            if e in ['', '.']:
                continue
            elif e == '..':
                if len(ret):
                    ret.pop()
            else:
                ret.append(e)
        return '/' + '/'.join(ret)
