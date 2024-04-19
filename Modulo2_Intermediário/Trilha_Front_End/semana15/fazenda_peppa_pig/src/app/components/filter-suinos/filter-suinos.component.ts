import { Component, EventEmitter, Input, Output, SimpleChanges } from '@angular/core';
import { type_suino } from '../../types/type_suino';
import { NgFor, NgIf } from '@angular/common';
import { FormsModule } from '@angular/forms';


@Component({
  selector: 'app-filter-suinos',
  standalone: true,
  imports: [NgIf, NgFor, FormsModule],
  templateUrl: './filter-suinos.component.html',
  styleUrl: './filter-suinos.component.css'
})
export class FilterSuinosComponent {
  @Input() suinos: type_suino[] = []; 
  @Output()  onFilteredSuinos = new EventEmitter<{ propriedade: keyof type_suino, valor:string }>();

  propriedades: (keyof type_suino)[] = ['Brinco', 'BrincoPai', 'BrincoMae', 'DataNascimento', 'DataSaida', 'Status', 'Sexo'];
  valoresUnicos: { [propriedade in keyof type_suino]: any[] } = {} as any;
  optionSelected:any = { propriedade: null, valor: null };

  ngOnChanges(changes: SimpleChanges) {


    if (changes["suinos"].currentValue.length > 0) {
      this.inicializarValoresUnicos();

    }

  }

  inicializarValoresUnicos() {
    this.propriedades.forEach(propriedade => {
      this.valoresUnicos[propriedade] = this.obterValoresUnicos(propriedade);
    });
  }

  obterValoresUnicos(propriedade: keyof type_suino): any[] {
    return this.suinos.map(suino => suino[propriedade])
      .filter((value, index, self) => self.indexOf(value) === index);
  }

  atualizarOptionSelected(propriedade: keyof type_suino, event: any) {
    this.optionSelected.propriedade = propriedade;
    this.optionSelected.valor = event.target.value;

    this.onFilteredSuinos.emit(this.optionSelected)
  }
}
