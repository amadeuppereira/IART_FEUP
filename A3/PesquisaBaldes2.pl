%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%     Search Algorithm  - Nodes have the form: S+D+F+A
%%%            where S describes the state or configuration
%%%                  D is the depth of the node
%%%                  A is the ancestor list for the node
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%:- op(400,yfx,'#').    % Node builder notation

s:- estado_ini(State),
    search([State+0+0+[]],S),
    reverse(S,Sol),
    write(Sol).

search([State+_+_+Soln|_], Soln) :- estado_obj(State).
search([B|R],S) :-
    expand(B,Children),
    insert_all(Children,R,Open),
    search(Open,S).

insert_all([F|R],Open1,Open3) :-
    insert(F,Open1,Open2),
    insert_all(R,Open2,Open3).
insert_all([],Open,Open).

insert(B,Open,Open) :- repeat_node(B,Open), ! .
insert(B,[C|R],[B,C|R]) :- cheaper(B,C), ! .
insert(B,[B1|R],[B1|S]) :- insert(B,R,S), !.
insert(B,[],[B]).

repeat_node(P+_+_+_, [P+_+_+_|_]).
cheaper( _+_+F1+_ , _+_+F2+_ ):- F1 < F2.

expand(State+D+_+S,MyChildren):-
     bagof(Child+D+F+[Move|S],
             (operador(Move,State,Child,Custo),
              F is D+Custo),
           MyChildren).  %write(MyChildren), nl.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%  Codigo Especifico Problema dos Baldes
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%cap(C1/C2), estado_ini(B1/B2), estado_obj(N1,N2).
cap(4/3).
estado_ini(0/0).
estado_obj(2/_).
%operador(Nome, EstIni, EstFin, Custo).
operador(d12a, B1/B2, B1F/C2, 1):-
	cap(_/C2), B1>0, B2<C2, B1>=C2-B2, B1F is B1-(C2-B2).
operador(d12b, B1/B2, 0/B2F, 1):-
	cap(_/C2), B1>0, B2<C2, B1<C2-B2, B2F is B1+B2.
operador(d21a, B1/B2, C1/B2F, 1):-
	cap(C1/_), B2>0, B1<C1, B2>=C1-B1, B2F is B2-(C1-B1).
operador(d21b, B1/B2, B1F/0, 1):-
	cap(C1/_), B2>0, B1<C1, B2<C1-B1, B1F is B1+B2.
operador(enc1, B1/B2, C1/B2, 1):- cap(C1/_), B1<C1.
operador(enc2, B1/B2, B1/C2, 1):- cap(_/C2), B2<C2.
operador(esv1, B1/B2, 0/B2, 1):- B1>0.
operador(esv2, B1/B2, B1/0, 1):- B2>0.
