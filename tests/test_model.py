def test_accuracy_threshold():
    with open("model/artifacts/accuracy.txt", "r") as f:
        accuracy = float(f.read())

    assert accuracy >= 0.94, f"❌ Accuracy too low: {accuracy}"             
