function index(array, n){
    return ((n > array.length - 1) ? -1 : Math.pow(array[n], n));
}

/*
Test.describe("Basic tests",_=>{
Test.assertEquals(index([1, 2, 3, 4],2),9);
Test.assertEquals(index([1, 3, 10, 100],3),1000000);
Test.assertEquals(index([0, 1],0),1);
Test.assertEquals(index([1, 2],3),-1);
Test.assertEquals(index([0], 0),1);
Test.assertEquals(index([1,1,1,1,1,1,1,1,1,1], 9),1);
Test.assertEquals(index([1,1,1,1,1,1,1,1,1,2], 9),512);
Test.assertEquals(index([29,82,45,10], 3),1000);
Test.assertEquals(index([6,31], 3),-1);
Test.assertEquals(index([75,68,35,61,9,36,89,0,30], 10),-1);
})
*/