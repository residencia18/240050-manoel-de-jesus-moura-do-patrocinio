import { DatePipe } from '@angular/common';
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'formatdate',
  standalone: true
})
export class FormatdatePipe implements PipeTransform {

  transform(value: any): any {
    const datePipe = new DatePipe('en-US');
    return datePipe.transform(value, 'dd/MM/yyyy');
  }
}
 