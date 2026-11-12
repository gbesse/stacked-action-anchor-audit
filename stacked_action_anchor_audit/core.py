from .common import number,integer
def run(data):
 states=data['states'];deltas=data['observation_deltas'];actions=data['actions']
 if not isinstance(states,list)or not 1<=len(states)<=1000 or len(deltas)!=len(states)or len(set(deltas))!=len(deltas)or deltas.count(0)!=1:raise ValueError('stack')
 for d in deltas:integer(d,-10000,10000)
 width=len(states[0])
 if not 1<=width<=1000 or any(len(s)!=width for s in states)or not isinstance(actions,list)or len(actions)>1000 or any(len(a)!=width for a in actions):raise ValueError('dimensions')
 states=[[number(v,-1e9,1e9)for v in s]for s in states];actions=[[number(v,-1e9,1e9)for v in a]for a in actions];current=deltas.index(0)
 def relative(index):return [[a[j]-states[index][j]for j in range(width)]for a in actions]
 old=relative(0);correct=relative(current);roundtrip=[[r[j]+states[0][j]for j in range(width)]for r in old]
 return {'first_index_delta':deltas[0],'current_index':current,'first_anchor_relative':old,'current_anchor_relative':correct,'legacy_roundtrip_matches':all(abs(a-b)<1e-8 for x,y in zip(actions,roundtrip)for a,b in zip(x,y)),'anchor_current':current==0,'upstream_policy_executed':False}
