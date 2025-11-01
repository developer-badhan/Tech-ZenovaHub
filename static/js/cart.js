// Copy SKU to clipboard
function copySKU(sku) {
    navigator.clipboard.writeText(sku).then(function() {
        var toast = new bootstrap.Toast(document.getElementById('copyToast'));
        toast.show();
    }).catch(function(err) {
        alert('Failed to copy SKU: ' + err);
    });
}

// opener functions bind expected SKU + product name to modal
function openUpdateModal(expectedSku, productName) {
    document.getElementById('updateTargetName').textContent = productName || '';
    document.getElementById('updateExpectedSKU').value = expectedSku || '';
    document.getElementById('updateSKUInput').value = '';
    document.getElementById('updateQuantity').value = 1;
    document.getElementById('updateValidation').style.display = 'none';
    document.getElementById('updateSKUInput').classList.remove('is-invalid');

    var updateModal = new bootstrap.Modal(document.getElementById('updateModal'));
    updateModal.show();
    setTimeout(function(){ document.getElementById('updateSKUInput').focus(); }, 200);
}

function openRemoveModal(expectedSku, productName) {
    document.getElementById('removeTargetName').textContent = productName || '';
    document.getElementById('removeExpectedSKU').value = expectedSku || '';
    document.getElementById('removeSKUInput').value = '';
    document.getElementById('removeValidation').style.display = 'none';
    document.getElementById('removeSKUInput').classList.remove('is-invalid');

    var removeModal = new bootstrap.Modal(document.getElementById('removeModal'));
    removeModal.show();
    setTimeout(function(){ document.getElementById('removeSKUInput').focus(); }, 200);
}

// client-side validation to avoid obvious mistakes
document.getElementById('updateForm').addEventListener('submit', function(e){
    var expected = (document.getElementById('updateExpectedSKU').value || '').trim();
    var pasted = (document.getElementById('updateSKUInput').value || '').trim();
    if (!pasted) {
        e.preventDefault();
        showUpdateValidation('Please paste the SKU for the item you want to update.');
        return;
    }
    if (pasted.toLowerCase() !== expected.toLowerCase()) {
        e.preventDefault();
        showUpdateValidation('SKU mismatch. Make sure you pasted the SKU displayed for the target item.');
        return;
    }
    // allowed to submit
});

function showUpdateValidation(msg) {
    var el = document.getElementById('updateValidation');
    el.style.display = 'block';
    el.textContent = msg;
    document.getElementById('updateSKUInput').classList.add('is-invalid');
}

document.getElementById('updateSKUInput').addEventListener('input', function(){
    document.getElementById('updateSKUInput').classList.remove('is-invalid');
    document.getElementById('updateValidation').style.display = 'none';
});

document.getElementById('removeForm').addEventListener('submit', function(e){
    var expected = (document.getElementById('removeExpectedSKU').value || '').trim();
    var pasted = (document.getElementById('removeSKUInput').value || '').trim();
    if (!pasted) {
        e.preventDefault();
        showRemoveValidation('Please paste the SKU for the item you want to remove.');
        return;
    }
    if (pasted.toLowerCase() !== expected.toLowerCase()) {
        e.preventDefault();
        showRemoveValidation('SKU mismatch. Make sure you pasted the SKU displayed for the target item.');
        return;
    }
    // allowed to submit
});

function showRemoveValidation(msg) {
    var el = document.getElementById('removeValidation');
    el.style.display = 'block';
    el.textContent = msg;
    document.getElementById('removeSKUInput').classList.add('is-invalid');
}

document.getElementById('removeSKUInput').addEventListener('input', function(){
    document.getElementById('removeSKUInput').classList.remove('is-invalid');
    document.getElementById('removeValidation').style.display = 'none';
});