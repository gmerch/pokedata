class Pokemon:
    def __init__(self, pokemon, item, ability, evs, ivs, nature, moves,shiny=False, nickname=None,level=50):
        self.nickname = nickname
        self.pokemon = pokemon
        self.item = item
        self.ability = ability
        self.evs = evs
        self.ivs = ivs
        self.nature = nature
        self.moves = moves
        self.shiny = shiny
        self.level = level


    def __repr__(self):
        print_base = f''
        if self.nickname:
            print_base += f'{self.nickname} '
        print_base += self.pokemon
        if self.item:
            print_base += f' @ {self.item}'
        print_base += f'\nAbility: {self.ability} \nLevel: {self.level}\n'
        if self.evs:
            ev_base = ''
            for ev, val in self.evs.items():
                if val >= 0:
                    ev_base += f' {val} {ev} /'
            print_base += f'EVs: {ev_base[:-2]} \n'
        print_base += f'{self.nature} Nature \n'
        if self.ivs:
            iv_base = ''
            for iv, val in self.ivs.items():
                if val != 31:
                    iv_base += f' {val} {iv} /'
            print_base += f'IVs: {iv_base[:-2]} \n'
        for move in self.moves:
            print_base += f'- {move} \n'
        return print_base