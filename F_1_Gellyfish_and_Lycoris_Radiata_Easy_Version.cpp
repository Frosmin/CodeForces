using namespace std;
using ll = long long;
 
vector<int> L, R, T, sz, head, tail, lazy, stat;
vector<int> que, nxt;
int root, dead[300300];
 
int newnode(int l, int r){
    // printf(" newnode %d %d\n", sz[l], sz[r]);
    if (!l && r) return r;
    if (l && !r) return l;
    int ret = L.size();
    L.push_back(l);
    R.push_back(r);
    T.push_back(0);
    sz.push_back(sz[l] + sz[r]);
    head.push_back(que.size());
    tail.push_back(que.size());
    lazy.push_back(0);
    que.push_back(0);
    nxt.push_back(-1);
    stat.push_back(0);
 
    if (l){
        nxt[tail[l]] = que.size();
        tail[l] = que.size();
        que.push_back(ret);
        nxt.push_back(-1);
    }
 
    if (r){
        nxt[tail[r]] = que.size();
        tail[r] = que.size();
        que.push_back(ret);
        nxt.push_back(-1);
    }
 
    return ret;
}
 
int newtag(int x, int val){
    int ret = L.size();
    L.push_back(0);
    R.push_back(0);
    T.push_back(val);
    sz.push_back(0);
    head.push_back(que.size());
    tail.push_back(que.size());
    lazy.push_back(0);
    que.push_back(0);
    nxt.push_back(-1);
    stat.push_back(-1);
 
    nxt[tail[x]] = que.size();
    tail[x] = que.size();
    que.push_back(ret);
    nxt.push_back(-1);
 
    return ret;
}
 
void push(int x){
    if (!x || !lazy[x]) return;
    swap(L[x], R[x]);
    lazy[L[x]] ^= 1, lazy[R[x]] ^= 1;
    lazy[x] = 0;
}
 
int good(int x, int y){
    return x*5 > x+y && y*5 > x+y;
}
 
int merge(int x, int y){
    if (!y) return x;
    if (!x) return y;
    push(x); push(y);
 
    if (good(sz[x], sz[y])) return newnode(x, y);
    
    if (sz[x] > sz[y]){
        int p = L[x];
        int q = merge(R[x], y);
        stat[x] = -1;
        if (good(sz[p], sz[q])) return newnode(p, q);
        stat[q] = -1;
        if (good(sz[p], sz[L[q]]) && good(sz[p] + sz[L[q]], sz[R[q]])) return newnode(newnode(p, L[q]), R[q]);
        push(L[q]);
        stat[L[q]] = -1;
        return newnode(newnode(p, L[L[q]]), newnode(R[L[q]], R[q]));
    }
    
    else{
        int p = merge(x, L[y]);
        int q = R[y];
        stat[y] = -1;
        if (good(sz[p], sz[q])) return newnode(p, q);
        stat[p] = -1;
        if (good(sz[R[p]], sz[q]) && good(sz[L[p]], sz[R[p]] + sz[q])) return newnode(L[p], newnode(R[p], q));
        push(R[p]);
        stat[R[p]] = -1;
        return newnode(newnode(L[p], L[R[p]]), newnode(R[R[p]], q));
    }
}
 
array<int, 2> split(int cur, int k){
    push(cur);
    assert(0 <= k && k <= sz[cur]);
 
    if (k==0) return {0, cur};
    if (k==sz[cur]) return {cur, 0};
 
    stat[cur] = -1;
 
    if (k <= sz[L[cur]]){
        int z = R[cur];
        auto [x, y] = split(L[cur], k);
        return {x, merge(y, z)};
    }
 
    else{
        int x = L[cur];
        auto [y, z] = split(R[cur], k - sz[L[cur]]);
        return {merge(x, y), z};
    }
}
 
void insert(int r, int val){
    auto [x, y] = split(root, r);
    newtag(x, val);
    root = merge(x, y);
}
 
void rev(int r){
    auto [x, y] = split(root, r);
    push(x);
    lazy[x] ^= 1;
    root = merge(x, y);
}
 
int _query(int cur){
    if (stat[cur]==-2) return 0;
    if (dead[T[cur]]) T[cur] = 0;
    if (T[cur]) return T[cur];
    while(true){
        int par = que[head[cur]];
        int ret = par?_query(par):0;
        
        if (ret) return ret;
        if (head[cur]==tail[cur]) break;
 
        head[cur] = nxt[head[cur]];
    }
 
    if (stat[cur]==-1){
        stat[cur] = -2;
    }
 
    return 0;
}
 
int query(int p){
    int cur = root;
    while(true){
        push(cur);
        int nxt = 0;
        
        if (p > sz[L[cur]]) nxt = R[cur], p -= sz[L[cur]];
        else nxt = L[cur];
        
        if (!nxt) break;
        cur = nxt;
    }
 
    return _query(cur);
}
 
int build(int l, int r){
    if (l==r){
        int leaf = newnode(0, 0);
        sz[leaf] = 1;
        return leaf;
    }
 
    int mid = (l+r)>>1;
    return newnode(build(l, mid), build(mid+1, r));
}
 
void init(int n){
    L.push_back(0);
    R.push_back(0);
    T.push_back(0);
    sz.push_back(0);
    head.push_back(-1);
    tail.push_back(-1);
    lazy.push_back(0);
    que.push_back(0);
    nxt.push_back(-1);
 
    root = build(1, n);
}
mt19937_64 gen(1557);
 
ll getrand(ll l, ll r){
    uniform_int_distribution<ll> tmp(l, r);
    return tmp(gen);
}
 
int main(){
    int n, q;
    scanf("%d %d", &n, &q);
    init(n);
 
    int prv = 0;
    for (int i=1;i<=q;i++){
        int op, x, y;
        scanf("%d %d %d", &op, &x, &y);
        // op = getrand(1, 3);
        // if (op <= 2) x = getrand(1, n);
        // else x = getrand(1, q);
        // y = getrand(1, n);
        
        if (op==1){
            x = (x + prv - 1) % n + 1;
            // printf(" op %d %d %d\n", op, x, y);
            insert(x, i);
        }
        if (op==2){
            x = (x + prv - 1) % n + 1;
            // printf(" op %d %d %d\n", op, x, y);
            rev(x);
        }
        if (op==3){
            x = (x + prv - 1) % q + 1;
            // printf(" op %d %d %d\n", op, x, y);
            if (x <= i) dead[x] = 1;
        }
 
        int ans = query((y + prv - 1) % n + 1);
        printf("%d\n", ans);
        prv = ans;
 
        // assert(sz[root] == n);
    }
}