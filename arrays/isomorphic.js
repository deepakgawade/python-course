const isoMap = new Map();

let s1="bada"
let s2="bcda"

var isomorphic=function(s,t){

    let sLen=s.length;
    let tLen=t.length;
    if(sLen!=tLen){
        return false;
    }
    for(let i=0;i<sLen;i++){
        let char1=s[i];
        let char2=t[i];

        if (isoMap.has(char1)){
            if(isoMap.get(char1)==char2){
                continue;
            }
            else{
                return false;
            }
        }else{

            isoMap.set(char1,char2)
        }


    }
    return true;
}

console.log(isomorphic(s1,s2))


