var startDatePicker;
var endDatePicker;
var startDate;
var endDate;

window.onload = function() {
    function pikadayCalender(){
        startDatePicker = new Pikaday({ field: document.getElementById('start-date'),
                                        minDate: moment().toDate(),
                                        format: 'YYYY/MM/DD'});
        endDatePicker = new Pikaday({ field: document.getElementById('end-date'),
                                        format: 'YYYY/MM/DD'});
        startDatePicker.setMinDate(new Date());
        endDatePicker.setMinDate(new Date())
        startDatePicker._o.onSelect = function(date){
            endDatePicker.setMinDate(date);
        }
        endDatePicker._o.onSelect = function(date){
            startDatePicker.setMaxDate(date);
        }
    }
    pikadayCalender();
}

function getAvailableCars(selection, start,end){
var startList = start.split(' ');
var endList = end.split(' ');



fetch(`http://localhost:8000/product/availableCars?carPrice=${selection}&startDate=${startList[3]}-${getMonthNumber(startList[1])}-${startList[2]}&endDate=${endList[3]}-${getMonthNumber(endList[1])}-${endList[2]}`)
.then(info => info.json())
.then(info => {


    var oldDiv = document.getElementById('belowDiv');
    while (oldDiv.firstChild) {
        oldDiv.removeChild(oldDiv.firstChild);
    }
    for (item in info){
    if (item === 'start-date' || item === 'end-date'){
        continue;
    }
    
        
    var newDiv = document.createElement('div');
    if (item == 'error'){
        var error = document.createElement('h1');
        error.textContent = info['error'];
        newDiv.appendChild(error);
        oldDiv.appendChild(newDiv);
        
        break;
    }
       

    var h1 = document.createElement('h1');
    var link = document.createElement('a');
    var id = info[item];
    
    link.href = `${id}/${info['start-date']}/${info['end-date']}`;
    link.textContent = `Reserve ${item}`;
    h1.textContent = item;
    newDiv.appendChild(h1);
    newDiv.appendChild(link);

    

    oldDiv.appendChild(newDiv);
    }


    

})
.catch(err =>{
    console.log(err);
})

}



document.getElementById('enterButton').addEventListener('click', function(event){
    getAvailableCars(document.getElementById('selection').value, document.getElementById('start-date').value, document.getElementById('end-date').value)
});



function getMonthNumber(month){
    if (month === 'Jan'){
        return 1;
    }
    if (month === 'Feb'){
        return 2;
    }
    if (month === 'Mar'){
        return 3;
    }
    if (month === 'Apr'){
        return 4;
    }
    if (month === 'May'){
        return 5;
    }
    if (month === 'Jun'){
        return 6;
    }
    if (month === 'Jul'){
        return 7;
    }
    if (month === 'Aug'){
        return 8;
    }
    if (month === 'Sep'){
        return 9;
    }
    if (month === 'Oct'){
        return 10;
    }
    if (month === 'Nov'){
        return 11;
    }
    if (month === 'Dec'){
        return 12;
    }
}


