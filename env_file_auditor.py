import argparse, json

def audit(text):
 seen=set(); issues=[]
 for n,line in enumerate(text.splitlines(),1):
  line=line.strip()
  if not line or line.startswith('#'): continue
  if '=' not in line: issues.append({'line':n,'issue':'missing_equals'}); continue
  key,value=line.split('=',1); key=key.strip()
  if key in seen: issues.append({'line':n,'issue':'duplicate_key','key':key})
  seen.add(key)
  if not value.strip(): issues.append({'line':n,'issue':'blank_value','key':key})
 return issues

def main():
 p=argparse.ArgumentParser(); p.add_argument('file'); a=p.parse_args()
 with open(a.file,encoding='utf8') as f: print(json.dumps(audit(f.read()),indent=2))
if __name__=='__main__': main()
